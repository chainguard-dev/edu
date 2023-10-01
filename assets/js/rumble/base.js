import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

// check for local advisory data that is less than 24 hours old
async function fetchAdvisories() {
    let res = await fetch("https://storage.googleapis.com/chainguard-academy/vulnerability-info/security.json");
    if (res.ok) {
        let advisoryData = await res.json();
        advisoryData["date"] = new Date().getTime();
        return advisoryData;
    } else {
        return null;
    }
};

// colour coding for sevrity on vulnerabilty info pages
const severityColours = {
    Critical: "#F236F6",
    High: "#3443F4",
    Medium: "#1F2892",
    Low: "#16C0D7",
    Negligible: "#C5C5C5",
    Unknown: "#8C8C8C"
}

// used on image comparison and vulnerability info page search fields
const searchFilter = document.querySelector("#filterInput");
const severityPicker = document.querySelector("#severity-picker");
if (searchFilter !== null) {
    searchFilter.value = null;
    searchFilter.addEventListener("keyup", () => {
        let filter = document.getElementById("filterInput").value.toLowerCase();
        filterTable("rumble-images-external", filter);
        filterTable("rumble-images-chainguard", filter);
        if (severityPicker != null) {
            severityPicker.querySelector("label span").innerHTML = `<span>Severity<span class="bi-chevron-down" style="padding-left: 2rem;"></span></span>`;
        }
    });
}

// taken from https://www.delftstack.com/howto/javascript/javascript-filter-table/
function filterTable(tableId, filter) {
    var table, tr, i, j;
    table = document.getElementById(tableId);
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
        tr[i].style.display = "none";
        const tdArray = tr[i].getElementsByTagName("td");
        for (var j = 0; j < tdArray.length; j++) {
            const cellValue = tdArray[j];
            if (cellValue && cellValue.innerHTML.toLowerCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                break;
            }
        }
    }
}
