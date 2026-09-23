// Copy buttons for the command blocks. The page works without this file.
document.documentElement.classList.remove("no-js");

function flash(button, label) {
  if (button.dataset.busy) {
    return;
  }
  button.dataset.busy = "1";
  var original = button.dataset.label || button.textContent;
  button.dataset.label = original;
  button.textContent = label;
  button.setAttribute("aria-label", label);
  window.setTimeout(function () {
    button.textContent = original;
    button.setAttribute("aria-label", button.dataset.title);
    delete button.dataset.busy;
  }, 1500);
}

document.querySelectorAll("button[data-copy]").forEach(function (button) {
  button.dataset.title = button.getAttribute("aria-label");
  button.addEventListener("click", function () {
    var target = document.getElementById(button.dataset.copy);
    if (!target) {
      return;
    }
    var text = target.textContent.trim();
    if (!navigator.clipboard) {
      flash(button, "Select and copy");
      return;
    }
    navigator.clipboard.writeText(text).then(
      function () { flash(button, "Copied"); },
      function () { flash(button, "Select and copy"); }
    );
  });
});
