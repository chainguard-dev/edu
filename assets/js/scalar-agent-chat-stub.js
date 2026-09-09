// Build-time stub for @scalar/agent-chat.
//
// The API reference sets `agent: { disabled: true }` in scalar-api-reference.js,
// so Scalar's AI chat drawer never mounts. Scalar lazy-loads the chat through a
// dynamic import, but Hugo's js.Build emits a single bundle with no code
// splitting, so esbuild inlines it regardless — pulling the whole Vercel AI SDK
// into the script served on every API spec page.
//
// Shimming the package to this file drops that subtree from the bundle. If the
// agent chat is ever enabled, delete this file and the matching `shims` entry in
// layouts/shortcodes/openapi.html.

export const Chat = {
  name: "ScalarAgentChatDisabled",
  render: () => null,
};
