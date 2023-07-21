export const app$frame = hook("frame");

export function hook(hook, name) {
  [hook, name] = typeof hook === "string" ? [() => {}, hook] : [hook, name];
  return function (...params) {
    this[`_${name}`].push([hook, ...params]);
    return this;
  };
}
