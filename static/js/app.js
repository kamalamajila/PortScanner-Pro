document.addEventListener("DOMContentLoaded", () => {
    const navToggle = document.getElementById("navToggle");
    const navbar = document.getElementById("navbar");
    const scanMode = document.getElementById("scan_mode");
    const customRangeFields = document.getElementById("customRangeFields");
    const portSearch = document.getElementById("portSearch");
    const portsTable = document.getElementById("portsTable");

    if (navToggle && navbar) {
        navToggle.addEventListener("click", () => {
            navbar.classList.toggle("show");
        });
    }

    function updateCustomFields() {
        if (!scanMode || !customRangeFields) return;
        const isCustom = scanMode.value === "custom";
        customRangeFields.style.display = isCustom ? "grid" : "none";
    }

    if (scanMode) {
        updateCustomFields();
        scanMode.addEventListener("change", updateCustomFields);
    }

    if (portSearch && portsTable) {
        const rows = portsTable.querySelectorAll("tbody tr");

        portSearch.addEventListener("input", (e) => {
            const query = e.target.value.toLowerCase().trim();

            rows.forEach((row) => {
                const text = row.textContent.toLowerCase();
                row.classList.toggle("hide-row", !text.includes(query));
            });
        });
    }
});