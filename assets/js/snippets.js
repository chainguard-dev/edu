const removeCopyButton = (pre) => {
  const copyButton = pre.querySelector(".btn.btn-copy");
  pre.removeChild(copyButton);
};

function toast(textContent) {
  const notification = document.getElementById("notification");
  const notificationText = document.getElementById("notification-text");
  notificationText.textContent = textContent;
  notification.classList.remove("notification-toast");
  requestAnimationFrame(() => notification.classList.add("notification-toast"));
}

const expandCode = (expanded, codeContent, expandButtonText, expandIcon) => {
  if (expanded) {
    expandButtonText.textContent = "Expand code";
    codeContent.classList.add("code-collapsed");
    expandIcon.classList.remove("expand-btn-icon-expanded");
    expandIcon.classList.add("expand-btn-icon-collapsed");
  } else {
    expandButtonText.textContent = "Collapse code";
    codeContent.classList.remove("code-collapsed");
    expandIcon.classList.remove("expand-btn-icon-collapsed");
    expandIcon.classList.add("expand-btn-icon-expanded");
  }
};

const customizeUI = (pre) => {
  removeCopyButton(pre); // remove original copy button
  const codeContent = pre.querySelector("code");
  codeContent.classList.add("code");

  pre.classList.add("pre-container");

  const snippetTopContainer = document.createElement("div");
  snippetTopContainer.classList.add(
    "d-flex",
    "flex-row-reverse",
    "align-items-center",
    "top-container"
  );

  const actionContainer = document.createElement("div");
  actionContainer.classList.add("d-flex");
  // const languageList = document.createElement("select");
  const language = codeContent.getAttribute("data-lang");
  // if (language) {
  //   languageList.classList.add("language-selector");
  //   const languageItem = document.createElement("option");
  //   languageItem.textContent = language;
  //   const bashLanguages = ["shell", "sh"];
  //   if (bashLanguages.includes(language)) {
  //     languageItem.textContent = "Bash";
  //   }
  //   languageList.append(languageItem);
  //   actionContainer.append(languageList);
  // } else {
  const output = document.createElement("span");
  output.classList.add("language-selector");
  output.textContent = language || "Output";
  actionContainer.append(output);
  // }

  const copyButton = document.createElement("button");
  copyButton.classList.add("tooltip-container");
  const copyIcon = document.createElement("i");
  copyIcon.classList.add("bi", "bi-files");
  const copyText = document.createElement("span");
  copyText.textContent = "Copy";
  copyText.classList.add("tooltip");
  copyButton.append(copyIcon, copyText);

  copyButton.addEventListener("click", () => {
    const textToCopy = codeContent.innerText;

    navigator.clipboard
      .writeText(textToCopy)
      .then(() => {
        copyText.textContent = "Copied";
        setTimeout(() => {
          copyText.textContent = "Copy";
        }, 2000);
      })
      .catch((err) => {
        console.error("Failed to copy text:", err);
      });

    toast("Code copied to your clipboard");
  });
  actionContainer.append(copyButton);

  snippetTopContainer.append(actionContainer);
  pre.insertBefore(snippetTopContainer, pre.firstChild);
  const codeContentHeight = codeContent.offsetHeight - 48; // 48 = padding(24px) * 2
  const lineHeight = 22;
  let expanded = false;
  if (codeContentHeight / lineHeight > 6) {
    expanded = true;
    const expandButtonContainer = document.createElement("div");
    expandButtonContainer.classList.add("expand-btn-container");
    const expandButton = document.createElement("button");
    expandButton.classList.add("expand-btn");
    const expandButtonText = document.createElement("span");
    expandButtonText.textContent = "Expand code";
    const expandIcon = document.createElement("i");
    expandIcon.classList.add("bi", "bi-chevron-right");
    expandButton.append(expandButtonText, expandIcon);
    expandCode(expanded, codeContent, expandButtonText, expandIcon);
    expandButton.addEventListener("click", () => {
      expanded = !expanded;
      expandCode(expanded, codeContent, expandButtonText, expandIcon);
    });
    expandButtonContainer.append(expandButton);
    pre.append(expandButtonContainer);
  }
  // Wrap if code doesn't contain a table or ASCII art
  if (!/____|----/.test(codeContent.innerText)) {
    codeContent.classList.add("code-wrap");
  }
};

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre").forEach((pre) => customizeUI(pre));
});
