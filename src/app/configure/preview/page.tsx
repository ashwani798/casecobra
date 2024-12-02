import { db } from "@/db";
import { notFound } from "next/navigation";
import DesignPreview from "./DesignPreview";

interface PageProps {
  searchParams: {
    [key: string]: string | string[] | undefined;
  };
}

const Page = async ({ searchParams }: PageProps) => {
  const { id } = searchParams;

  if (!id || typeof id !== "string") {
    return notFound();
  }

  const configuration = await db.configuration.findUnique({
    where: { id },
  });

  if (!configuration) {
    return notFound();
  }

  return <DesignPreview configuration={configuration} />;
};

export default Page;

// import { db } from "@/db";
// import { notFound } from "next/navigation";
// import DesignPreview from "./DesignPreview";

// interface PageProps {
//   searchParams: {
//     [key: string]: string | string[] | undefined;
//   };
// }

// const Page = async ({ searchParams }: PageProps) => {
//   try {
//     const awaitedSearchParams = await Promise.resolve(searchParams);
//     const id = awaitedSearchParams.id;

//     if (!id || typeof id !== "string") {
//       return notFound();
//     }

//     const configuration = await db.configuration.findUnique({
//       where: { id },
//     });

//     if (!configuration) {
//       return notFound();
//     }

//     return <DesignPreview configuration={configuration} />;
//   } catch (error) {
//     console.error(
//       "Error resolving searchParams or fetching configuration:",
//       error
//     );
//     return notFound();
//   }
// };

// export default Page;
