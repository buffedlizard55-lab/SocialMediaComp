/* SocialMediaComp — static leaderboard renderer. No build step, no dependencies. */

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

async function load() {
  const [master, strat] = await Promise.all([
    fetch("data/master-list.json").then((r) => {
      if (!r.ok) throw new Error("master-list.json HTTP " + r.status);
      return r.json();
    }),
    fetch("data/strategies.json").then((r) => {
      if (!r.ok) throw new Error("strategies.json HTTP " + r.status);
      return r.json();
    }),
  ]);

  const rowsEl = document.getElementById("rows");
  const countEl = document.getElementById("count");
  const statsEl = document.getElementById("stats");
  const platformEl = document.getElementById("platform");
  const cohortEl = document.getElementById("cohort");
  const qEl = document.getElementById("q");
  const sortBtn = document.getElementById("sort-metric");

  // Rebuild the platform filter from the data so new platforms can't be missed.
  const platformSelect = document.getElementById("platform");
  const platforms = [...new Set(master.entries.map((e) => e.platform))].sort();
  platformSelect.innerHTML =
    '<option value="all">All</option>' +
    platforms
      .map((p) => `<option value="${esc(p)}">${esc(p === "X" ? "X (Twitter)" : p)}</option>`)
      .join("");

  let sortDir = 0; // 0 = insertion order, -1 = metric desc, 1 = metric asc

  function render() {
    const p = platformEl.value;
    const c = cohortEl.value;
    const q = qEl.value.trim().toLowerCase();
    let rows = master.entries.filter((e) => {
      if (p !== "all" && e.platform !== p) return false;
      if (c !== "all" && (e.cohort || "") !== c) return false;
      if (!q) return true;
      return [e.handle, e.owner, e.topic, e.platform, e.country || ""]
        .join(" ")
        .toLowerCase()
        .includes(q);
    });
    if (sortDir !== 0) {
      rows = rows.slice().sort((a, b) => sortDir * (a.metric_value - b.metric_value));
    }
    countEl.textContent = rows.length + " of " + master.entries.length + " entries";
    rowsEl.innerHTML = rows
      .map(
        (e) => `
      <tr${e.irregularity ? ' class="flagged"' : ""}>
        <td>${esc(e.id)}</td>
        <td>${esc(e.platform)}</td>
        <td>${esc(e.handle)}</td>
        <td>${esc(e.owner)}</td>
        <td>${esc(e.topic)}</td>
        <td>${esc(e.cohort || "—")}</td>
        <td>${esc(e.country || "—")}</td>
        <td>${esc(e.metric_value)}${
          typeof e.likes_billions === "number"
            ? `<br /><span class="sub">${esc(e.likes_billions)}B likes</span>`
            : ""
        }<br /><span class="sub">${esc(e.metric_label)}<br />${esc(e.snapshot_note)}</span></td>
        <td>
          <a href="${esc(e.profile_url)}" rel="noopener">Profile</a><br />
          <a href="${esc(e.source_url)}" rel="noopener">${esc(e.source_name)}</a>
        </td>
        <td class="flag">${esc(e.irregularity || "—")}</td>
      </tr>`
      )
      .join("");
  }

  platformEl.addEventListener("change", render);
  cohortEl.addEventListener("change", render);
  qEl.addEventListener("input", render);
  sortBtn.addEventListener("click", () => {
    sortDir = sortDir === 0 ? -1 : sortDir === -1 ? 1 : 0;
    sortBtn.textContent = sortDir === -1 ? "Metric ↓" : sortDir === 1 ? "Metric ↑" : "Metric ⇅";
    render();
  });

  // Stats bar
  const byPlatform = master.entries.reduce((acc, e) => {
    acc[e.platform] = (acc[e.platform] || 0) + 1;
    return acc;
  }, {});
  const flagged = master.entries.filter((e) => e.irregularity).length;
  statsEl.textContent =
    master.entries.length + " entries · " +
    Object.entries(byPlatform).map(([k, v]) => v + " " + k).join(" · ") +
    " · " + flagged + " flagged for review";

  // Flags summary (all flagged rows with links)
  document.getElementById("flag-summary").innerHTML = master.entries
    .filter((e) => e.irregularity)
    .map(
      (e) =>
        `<li><strong>${esc(e.platform)} ${esc(e.handle)}</strong> — ${esc(e.irregularity)} ` +
        `(<a href="${esc(e.source_url)}" rel="noopener">source</a>)</li>`
    )
    .join("");

  render();

  document.getElementById("official").innerHTML = strat.official_resources
    .map(
      (o) =>
        `<article class="card"><strong><a href="${esc(o.url)}" rel="noopener">${esc(o.name)}</a></strong><p>${esc(o.why)}</p></article>`
    )
    .join("");
  document.getElementById("patterns").innerHTML = strat.observed_patterns
    .map((p) => `<li><strong>${esc(p.pattern)}.</strong> ${esc(p.example)}. ${esc(p.note)}</li>`)
    .join("");
  document.getElementById("topics").innerHTML = strat.topics_with_public_demand
    .map((t) => `<li>${esc(t)}</li>`)
    .join("");
  document.getElementById("meta-limits").innerHTML = master.meta.limitations
    .map((t) => `<li>${esc(t)}</li>`)
    .join("");
}

load().catch((err) => {
  document.getElementById("count").textContent =
    "Could not load data files (open via GitHub Pages or a local server).";
  console.error(err);
});
