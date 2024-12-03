import { OurFileRouter } from "@/app/api/uploadthing/core";
import { generateReactHelpers } from "@uploadthing/react";

export const { useUploadThing, uploadFiles } =
  generateReactHelpers<OurFileRouter>();

// import { OurFileRouter } from "@/app/api/uploadthing/core";
// import {
//   generateUploadButton,
//   generateUploadDropzone,
// } from "@uploadthing/react";

// export const UploadButton = generateUploadButton<OurFileRouter>();
// export const UploadDropzone = generateUploadDropzone<OurFileRouter>();