const createToast = () => {
  const notification = document.createElement("div");
  notification.id = "notification";
  notification.setAttribute("aria-live", "polite");
  const icon = document.createElement("i");
  icon.classList.add("bi", "bi-check-circle-fill");
  icon.setAttribute("aria-hidden", "true");
  const message = document.createElement("span");
  notification.append(icon, message);
  document.body.append(notification);

  return (text) => {
    message.textContent = text;
    notification.classList.remove("notification-toast");
    requestAnimationFrame(() => notification.classList.add("notification-toast"));
    notification.addEventListener("animationend", () => {
      message.textContent = "";
    }, { once: true });
  };
};

// Function to normalize code block labels with consistent formatting
const normalizeCodeBlockLabel = (rawLabel) => {
  if (!rawLabel) {
    return ""; // Keep unlabeled blocks unlabeled
  }

  // Define transformation rules for existing labels only
  const labelTransforms = {
    // Shell variants
    "shell": "Shell",
    "sh": "Shell",
    "bash": "Shell",

    // Configuration formats
    "yaml": "YAML",
    "yml": "YAML",
    "json": "JSON",
    "xml": "XML",

    // Database
    "sql": "SQL",
    "mariadb": "SQL",
    "mysql": "SQL",
    "postgresql": "SQL",
    "postgres": "SQL",

    // Container formats
    "dockerfile": "Dockerfile",

    // Programming languages
    "python": "Python",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "typescript": "TypeScript",
    "ts": "TypeScript",

    // Output and diffs
    "diff": "Diff",
    // Output
    "output": "Output",
  };

  const lowerLabel = rawLabel.toLowerCase();

  // Return transformed label if defined, otherwise return original unchanged
  return labelTransforms[lowerLabel] || rawLabel;
};

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

const customizeUI = (pre, toast) => {
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
  output.textContent = normalizeCodeBlockLabel(language);
  actionContainer.append(output);
  // }

  const copyButton = document.createElement("button");
  copyButton.classList.add("tooltip-container");
  copyButton.setAttribute("aria-label", "Copy code to clipboard");
  const copyIcon = document.createElement("i");
  copyIcon.classList.add("bi", "bi-files");
  const copyText = document.createElement("span");
  copyText.textContent = "Copy";
  copyText.classList.add("tooltip");
  copyButton.append(copyIcon, copyText);

  let resetTimer;
  copyButton.addEventListener("click", () => {
    const textToCopy = codeContent.innerText;

    navigator.clipboard
      .writeText(textToCopy)
      .then(() => {
        copyText.textContent = "Copied";
        clearTimeout(resetTimer);
        resetTimer = setTimeout(() => {
          copyText.textContent = "Copy";
        }, 2000);
        toast("Copied to clipboard");
      })
      .catch((err) => {
        console.error("Failed to copy text:", err);
      });
  });
  actionContainer.append(copyButton);

  snippetTopContainer.append(actionContainer);
  pre.insertBefore(snippetTopContainer, pre.firstChild);
  const codeContentHeight = codeContent.offsetHeight - 48; // 48 = padding(24px) * 2
  const lineHeight = 22;
  let expanded = false;
  if (codeContentHeight / lineHeight > 25) {
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
  const toast = createToast();
  document.querySelectorAll("pre:not(.scalar-app pre)").forEach((pre) => customizeUI(pre, toast));
});
