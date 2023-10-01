// used on an image's vulnerability comparison page

const image = document.location.pathname.replace(/\/$/, "").split("/").pop();
const data = await d3.csv(`https://storage.googleapis.com/chainguard-academy/cve-data/${image}.csv`);
const displayColumns = ["Package", "Version", "Vulnerability", "Severity"];
const dataColumns = ["package", "version", "vulnerability", "s"];
const dataSorted = sortData();

updateRumbleColorScheme();

const advisories = await fetchAdvisories();
window.document.advisories = advisories;
window.document.dataSorted = dataSorted;

makeTable("#rumble-images-external", dataSorted.theirs, dataSorted.theirVulns);
makeTable("#rumble-images-chainguard", dataSorted.ours, dataSorted.ourVulns);

function sortData() {
  let theirs = [],
    ours = [];

  data.forEach(function (row) {
    if (row.image.startsWith("cgr.dev")) {
      ours.push(row);
    } else {
      theirs.push(row);
    }
  });

  let theirVulns = [];
  let ourVulns = [];

  theirs.forEach(function (row) {
    if (!(theirVulns.includes(row.vulnerability, 0))) {
      theirVulns.push(row.vulnerability)
    }
  })

  ours.forEach(function (row) {
    if (!(ourVulns.includes(row.vulnerability, 0))) {
      ourVulns.push(row.vulnerability)
    }
  })

  return { "theirs": theirs, "ours": ours, "theirVulns": theirVulns, "ourVulns": ourVulns }
};

function makeTable(id, sortedData, vulnIDs) {
  var table = d3.select(id).append("table"),
    thead = table.append("thead"),
    tbody = table.append("tbody");

  // append the header row
  thead.append("tr")
    .selectAll("th")
    .data(function () {
      return displayColumns.map(function (column) {
        if (column == "Vulnerability") {
          let count = vulnIDs.length;
          column = `ID [${count} unique]`
        }
        return column;
      })
    })
    .enter()
    .append("th")
    .text(function (column) { return column; });



  // create a row for each object in the data
  var rows = tbody.selectAll("tr")
    .data(sortedData)
    .enter()
    .append("tr");

  // create a cell in each row for each column
  rows.selectAll("td")
    .data(function (row) {
      return dataColumns.map(function (column) {
        let val = row[column];
        if (column == "vulnerability") {
          let isProd = getEnvUrl();
          if (isProd) {
            val = `<a href="/vulnerabilities/${val}">${val}</a>`
          } else {
            val = `<a href="/vulnerabilities/?id=${val}">${val}</a>`
          }
        }
        if (column == "s") {
          val = `<span style="color: ${severityColours[val]}; vertical-align: text-bottom; font-size: 8px; padding: 0.5rem; ">⬤</span><span style="vertical-align: text-bottom;">${val}</span>`
        }
        return { column: column, value: val };
      });
    })
    .enter()
    .append("td")
    .html(function (d) { return d.value; });

  if (vulnIDs.length == 0) {
    document.querySelector(id).insertAdjacentHTML("beforeend", `<p style="margin: 0; padding: 24px 8px;">No vulnerabilities detected</p>`);
    return;
  }
};

// toggles between absolute and ?id= URLs for each page when rendering table links
function getEnvUrl() {
  let host = document.location.host;
  if (host.match(`.+netlify.com.+`)) {
    return false
  } else if (host.match(`localhost:1313`)) {
    return false
  } else {
    return true
  }
};

severityPicker.addEventListener("click", function (event) {
  if (event.target.tagName == "INPUT" || event.target.tagName == "LABEL") {
    return;
  }
  severityPicker.querySelector(".dropdown-content").visiblity = "hidden";
  severityPicker.querySelector('input[type = "checkbox"]').checked = false;

  let filter = event.target.dataset.severity.toLowerCase();
  filterTable("rumble-images-external", filter);
  filterTable("rumble-images-chainguard", filter);

  if (event.target.dataset.severity == "") {
    severityPicker.querySelector("label span").innerHTML = `<span>Severity<span class="bi-chevron-down" style="padding-left: 2rem;"></span></span>`;
    return;
  }

  severityPicker.querySelector("label span").innerHTML = `<span data-severity="${event.target.dataset.severity}"><span class="severity sev-${event.target.dataset.severity.toLowerCase()}"
  data-severity="${event.target.dataset.severity}">⬤</span>${event.target.dataset.severity}</span>`;
  searchFilter.value = null;
});
severityPicker.addEventListener("mouseleave", function (event) {
  // severityPicker.querySelector(".dropdown-content").visiblity = "hidden";
  severityPicker.querySelector('input[type = "checkbox"]').checked = false;
});

const tds = document.querySelectorAll("#rumble .tables table tbody tr td");
tds.forEach(function (td) {
  let href = td.parentNode.childNodes[2].childNodes[0].href;

  td.addEventListener("click", function () {
    document.location = href;
  });

})

// this function tells the rumble iframe which colour scheme to use
function updateRumbleColorScheme() {
  let theme = localStorage.getItem("theme") || "dark";
  let rumble = document.querySelector("iframe");
  rumble.contentWindow.postMessage({"colorscheme":theme});
}
