// Opens the Kapa AI assistant when the page URL asks for it, so a link from
// an email or the marketing site can take a reader straight to the chat:
//
//   /docs/?ask-ai                                opens the assistant
//   /docs/?ask-ai&q=How+do+I+get+started          opens it with the question filled in
//   /docs/?ask-ai&q=How+do+I+get+started&submit   also sends the question
//
// Sending is opt-in per link. Without "submit", the reader decides whether to
// send the question, so a link someone else crafted can't make the assistant
// answer it the moment the page opens.
//
// This file loads before the Kapa widget script, which loads asynchronously.

// Kapa's preinitialization snippet, from
// https://docs.kapa.ai/integrations/website-widget/javascript-api/preinitialize
// It queues calls such as Kapa("open") until the widget has finished loading.
(function () {
  if (!window.Kapa) {
    const queuedKapa = function () {
      queuedKapa.c(arguments);
    };
    queuedKapa.q = [];
    queuedKapa.c = function (args) {
      queuedKapa.q.push(args);
    };
    window.Kapa = queuedKapa;
  }
})();

(function () {
  const params = new URLSearchParams(window.location.search);
  if (!params.has("ask-ai")) return;

  const question = params.get("q") || "";
  const sendQuestion = params.has("submit") && question !== "";
  window.Kapa("open", { mode: "ai", query: question, submit: sendQuestion });
})();
