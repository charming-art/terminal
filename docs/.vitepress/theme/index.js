// .vitepress/theme/index.js
import DefaultTheme from "vitepress/theme";
import Layout from "genji-theme-vitepress";
import {h} from "vue";
import * as Cell from "../../../dist/es/index.js";

// More props: https://genji-md.dev/reference/props
const props = {
  Theme: DefaultTheme,
  library: {
    Cell,
  },
};

export default {
  extends: DefaultTheme,
  Layout: () => h(Layout, props),
};
