/* This file will find any highlighted code with variables like %your-variable%
   and make it into an inline editable element. Any occurrence of the variable
   will get replaced in the page when it loses focus.
*/

// Need to wait until after highlight js is done
document.onreadystatechange = () => {
    if (document.readyState === "complete") {
        makeVarsEditable();
    }
    return;
};

function makeVarsEditable() {
    let codes = document.querySelectorAll("span.hljs-string")
    codes.forEach(element => {
        let m = element.textContent.match(/%.+?%/g);
        if (m === null || m.length === 0) {
            return;
        }

        // add a span around variables
        let newElem = `<span data-title="test" title="Click to edit" class="inline-variable">${m[0]}</span>`;
        element.innerHTML = element.innerHTML.replace(m[0], newElem);

        // make it editable
        let span = element.querySelector("span.inline-variable");
        span.contentEditable = true;

        // update any other occurrences of the variable
        span.addEventListener("blur", (event) => {
            updateVariable(m[0], event)
        })
    });
    return;
}

function updateVariable(matchingString, event) {
    document.body.innerHTML = document.body.innerHTML.replaceAll(`${matchingString}`, event.target.innerText);

    // need to call this again, since document.body has been replaced,
    // meaning and all event listeners are gone
    makeVarsEditable();
    return;
}
