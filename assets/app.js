async function load() {
  const [master, strat] = await Promise.all([
    fetch("data/master-list.json").then((r) => r.json()),
    fetch("data/strategies.json").then((r) => r.json()),
  ]);

  const rowsEl = document.getElementById("rows");
  const countEl = document.getElementById("count");
  const platformEl = document.getElementById("platform");
  const qEl = document.getElementById("q");

  function render() {
    const p = platformEl.value;
    const q = qEl.value.trim().toLowerCase();
    const rows = master.entries.filter((e) => {
      if (p !== "all" && e.platform !== p) return false;
      if (!q) return true;
      return [e.handle, e.owner, e.topic, e.platform].join(" ").toLowerCase().includes(q);
    });
    countEl.textContent = rows.length + " of " + master.entries.length + " entries";
    rowsEl.innerHTML = rows
      .map(
        (e) => `
      <tr>
        <td>${e.id}</td>
        <td>${e.platform}</td>
        <td>${e.handle}</td>
        <td>${e.owner}</td>
        <td>${e.topic}</td>
        <td>${e.metric_value}<br /><span style="color:#9aa8b6;font-size:0.75rem">${e.metric_label}<br />${e.snapshot_note}</span></td>
        <td>
          <a href="${e.profile_url}" rel="noopener">Profile</a><br />
          <a href="${e.source_url}" rel="noopener">${e.source_name}</a>
        </td>
        <td class="flag">${e.irregularity ? e.irregularity : "—"}</td>
      </tr>`
      )
      .join("");
  }

  platformEl.addEventListener("change", render);
  qEl.addEventListener("input", render);
  render();

  document.getElementById("official").innerHTML = strat.official_resources
    .map(
      (o) =>
        `<article class="card"><strong><a href="${o.url}" rel="noopener">${o.name}</a></strong><p>${o.why}</p></article>`
    )
    .join("");
  document.getElementById("patterns").innerHTML = strat.observed_patterns
    .map((p) => `<li><strong>${p.pattern}.</strong> ${p.example}. ${p.note}</li>`)
    .join("");
  document.getElementById("topics").innerHTML = strat.topics_with_public_demand
    .map((t) => `<li>${t}</li>`)
    .join("");
  document.getElementById("meta-limits").innerHTML = master.meta.limitations
    .map((t) => `<li>${t}</li>`)
    .join("");
}

load().catch((err) => {
  document.getElementById("count").textContent = "Could not load data files (open via GitHub Pages or a local server).";
  console.error(err);
});
