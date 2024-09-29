// For vite env.
export const isNode = typeof navigator === "undefined" ? true : false;

const userAgent = isNode ? "node" : navigator.userAgent;

export const isFireFox = userAgent.includes("Firefox");

export const isLegacyEdge = userAgent.includes("Edge");
