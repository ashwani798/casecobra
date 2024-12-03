import { db } from "@/db";
import { stripe } from "@/lib/stripe";
import { NextResponse } from "next/server";
import Stripe from "stripe";

export async function POST(req: Request) {
  try {
    const body = await req.text();
    const signature = req.headers.get("stripe-signature");

    if (!signature) {
      return new Response("Invalid signature", { status: 400 });
    }

    if (!process.env.STRIPE_WEBHOOK_SECRET) {
      throw new Error("Stripe webhook secret is not set");
    }

    const event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET
    );

    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object as Stripe.Checkout.Session;

        if (!session.customer_details?.email) {
          throw new Error("Missing user email");
        }

        const { userId, orderId } = session.metadata || {
          userId: null,
          orderId: null,
        };

        if (!userId || !orderId) {
          throw new Error("Invalid request metadata");
        }

        const billingAddress = session.customer_details?.address;
        const shippingAddress = session.shipping_details?.address;

        if (!billingAddress || !shippingAddress) {
          throw new Error("Missing address details");
        }

        await db.order.update({
          where: { id: orderId },
          data: {
            isPaid: true,
            shippingAddress: {
              create: {
                name: session.customer_details.name!,
                city: shippingAddress.city!,
                country: shippingAddress.country!,
                postalCode: shippingAddress.postal_code!,
                street: shippingAddress.line1!,
                state: shippingAddress.state || null,
              },
            },
            billingAddress: {
              create: {
                name: session.customer_details.name!,
                city: billingAddress.city!,
                country: billingAddress.country!,
                postalCode: billingAddress.postal_code!,
                street: billingAddress.line1!,
                state: billingAddress.state || null,
              },
            },
          },
        });
        break;
      }
      default:
        console.warn(`Unhandled event type: ${event.type}`);
    }

    return NextResponse.json({ result: event, ok: true });
  } catch (err) {
    console.error("Webhook Error:", err);
    return NextResponse.json(
      { message: "Something went wrong", ok: false },
      { status: 500 }
    );
  }
}
