import { NULL_VALUE } from "./app/constant.js";

export function wide(string) {
  const code = string.codePointAt(0);
  return [code + 0xf0000000, NULL_VALUE];
}
