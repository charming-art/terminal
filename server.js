import { createServer } from "vite";
import config from "./vite.config";

const PORT = 3001;

export default async function () {
  const server = await createServer({
    ...config,
    server: {
      ...config.server,
      open: false,
      port: PORT,
      strictPort: true,
    },
    mode: "test",
  });
  await server.listen();
  server.printUrls();

  process.env.TEST_PORT = PORT;

  return () => {
    server.close();
  };
}
