import {defineConfig} from "vitepress";
import config from "genji-theme-vitepress/config";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Charming Cell",
  description: "The creative coding language for ASCII Art",
  extends: config,
  themeConfig: {
    nav: [
      {text: "Home", link: "/"},
      {text: "Examples", link: "https://observablehq.com/d/18b3d6f3affff5bb"},
    ],
    sidebar: [
      {
        text: "Introduction",
        items: [
          {text: "What is Cell?", link: "/what-is-cell"},
          {text: "Getting started", link: "/get-started"},
        ],
      },
      {
        text: "Features",
        items: [
          {text: "Sketches", link: "/features/sketches"},
          {text: "Shapes", link: "/features/shapes"},
        ],
      },
      {text: "API Index", link: "/api-index"},
    ],
    socialLinks: [{icon: "github", link: "https://github.com/charming-art/cell"}],
  },
});
