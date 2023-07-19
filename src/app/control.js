export function app$call(interceptor, ...params) {
  interceptor.call(this, this, ...params);
  return this;
}
