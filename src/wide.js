import { NULL_VALUE } from "./constant";

export function wide(string) {
  const code = string.codePointAt(0);
  return [code + 0xf0000000, NULL_VALUE];
}
