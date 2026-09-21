/* SocialMediaComp — static leaderboard. No build step, no dependencies. */

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

function extLink(href, label) {
  return `<a href="${esc(href)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;
}

function fmt(n) {
  if (typeof n !== "number" || Number.isNaN(n)) return "—";
  // Keep Guinness exact counts (e.g. 9.018251). Only trim binary float noise.
  return String(Math.round(n * 1e6) / 1e6);
}

function median(nums) {
  const s = nums.slice().sort((a, b) => a - b);
  const mid = Math.floor(s.length / 2);
  if (!s.length) return null;
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}

function likesPerFollower(e) {
  if (typeof e.likes_billions !== "number" || typeof e.metric_value !== "number" || e.metric_value <= 0) {
    return null;
  }
  return (e.likes_billions * 1000) / e.metric_value;
}

function verifyLabel(v) {
  if (v === "list_table") return "Published list table";
  if (v === "wiki_article_infobox") return "Wikipedia article infobox";
  if (v === "guinness_record") return "Guinness World Records";
  return "See verification log";
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
  const batchEl = document.getElementById("batch");
  const qEl = document.getElementById("q");
  const sortBtn = document.getElementById("sort-metric");
  const flaggedEl = document.getElementById("flagged-only");
  const groupEl = document.getElementById("group-platform");
  const notesBtn = document.getElementById("toggle-notes");

  const platforms = [...new Set(master.entries.map((e) => e.platform))].sort();
  platformEl.innerHTML =
    '<option value="all">All</option>' +
    platforms.map((p) => `<option value="${esc(p)}">${esc(p === "X" ? "X (Twitter)" : p)}</option>`).join("");

  const batches = [...new Set(master.entries.map((e) => e.added_batch).filter((n) => n != null))].sort((a, b) => a - b);
  batchEl.innerHTML =
    '<option value="all">All</option>' +
    batches.map((b) => `<option value="${esc(b)}">Batch ${esc(b)}</option>`).join("");

  let sortDir = 0;
  let notesOpen = false;
  const openIds = new Set();

  function filtered() {
    const p = platformEl.value;
    const c = cohortEl.value;
    const b = batchEl.value;
    const q = qEl.value.trim().toLowerCase();
    const flaggedOnly = flaggedEl.checked;
    let rows = master.entries.filter((e) => {
      if (p !== "all" && e.platform !== p) return false;
      if (c !== "all" && (e.cohort || "") !== c) return false;
      if (b !== "all" && String(e.added_batch) !== b) return false;
      if (flaggedOnly && !e.irregularity) return false;
      if (!q) return true;
      return [
        e.handle, e.owner, e.topic, e.platform, e.country || "",
        e.growth_notes || "", e.irregularity || "", e.article_name || "",
        e.source_name || "",
      ].join(" ").toLowerCase().includes(q);
    });
    if (groupEl.checked) {
      rows = rows.slice().sort((a, b2) => {
        const plat = a.platform.localeCompare(b2.platform);
        if (plat !== 0) return plat;
        return b2.metric_value - a.metric_value;
      });
    } else if (sortDir !== 0) {
      rows = rows.slice().sort((a, b2) => sortDir * (a.metric_value - b2.metric_value));
    }
    return rows;
  }

  function detailHtml(e) {
    const article = e.article_url
      ? `<p>${extLink(e.article_url, e.article_name || "Second source")}</p>`
      : "";
    const flag = e.irregularity ? `<p><strong>Flag.</strong> ${esc(e.irregularity)}</p>` : "";
    const ratio = likesPerFollower(e);
    const ratioHtml = ratio == null
      ? ""
      : `<p>Approx. ${esc(fmt(ratio))} cumulative likes per follower, from the rounded likes and follower figures on this row. Not a recent rate.</p>`;
    return `
      <div class="details-panel">
        <p><span class="pill">${esc(verifyLabel(e.verification_type))}</span>
           <span class="pill">Batch ${esc(e.added_batch || "—")}</span></p>
        <p>${esc(e.growth_notes || "No growth note on this row.")}</p>
        ${ratioHtml}
        ${flag}
        ${article}
      </div>`;
  }

  function render() {
    const rows = filtered();
    countEl.textContent = rows.length + " of " + master.entries.length + " entries";
    rowsEl.innerHTML = rows.map((e) => {
      const open = notesOpen || openIds.has(e.id);
      const likes = typeof e.likes_billions === "number"
        ? `<span class="sub">${esc(e.likes_billions)}B likes</span>`
        : "";
      return `
        <tr class="${e.irregularity ? "flagged" : ""}">
          <td>${esc(e.id)}</td>
          <td>${esc(e.platform)}</td>
          <td>
            <span class="handle">${esc(e.handle)}</span>
            <span class="sub">${esc(e.owner)}</span>
            <span class="sub">${esc(e.country || "Country not in source")}</span>
          </td>
          <td>${esc(e.topic)}</td>
          <td>${esc(e.cohort || "—")}</td>
          <td>${esc(e.metric_value)}
            ${likes}
            <span class="sub">${esc(e.metric_label)}<br />${esc(e.snapshot_note)}</span>
          </td>
          <td>
            ${extLink(e.profile_url, "Profile")}<br />
            ${extLink(e.source_url, "Source")}
            <br /><button type="button" class="details-btn" data-id="${esc(e.id)}" aria-expanded="${open ? "true" : "false"}" aria-label="${open ? "Hide notes" : "Notes"} for ${esc(e.handle)}">${open ? "Hide" : "Notes"}</button>
          </td>
          <td class="flag">${e.irregularity ? `<span class="flag-clip">${esc(e.irregularity)}</span>` : "—"}</td>
        </tr>
        <tr class="details-row" ${open ? "" : "hidden"}>
          <td colspan="8">${detailHtml(e)}</td>
        </tr>`;
    }).join("");
  }

  rowsEl.addEventListener("click", (ev) => {
    const btn = ev.target.closest(".details-btn");
    if (!btn) return;
    const id = Number(btn.getAttribute("data-id"));
    if (openIds.has(id)) openIds.delete(id);
    else openIds.add(id);
    notesOpen = false;
    notesBtn.textContent = "Show notes";
    render();
  });

  platformEl.addEventListener("change", render);
  cohortEl.addEventListener("change", render);
  batchEl.addEventListener("change", render);
  qEl.addEventListener("input", render);
  flaggedEl.addEventListener("change", render);
  groupEl.addEventListener("change", () => {
    if (groupEl.checked) {
      sortDir = 0;
      sortBtn.textContent = "Metric ⇅";
    }
    render();
  });
  sortBtn.addEventListener("click", () => {
    sortDir = sortDir === 0 ? -1 : sortDir === -1 ? 1 : 0;
    sortBtn.textContent = sortDir === -1 ? "Metric ↓" : sortDir === 1 ? "Metric ↑" : "Metric ⇅";
    if (sortDir !== 0) groupEl.checked = false;
    render();
  });
  notesBtn.addEventListener("click", () => {
    notesOpen = !notesOpen;
    if (!notesOpen) openIds.clear();
    notesBtn.textContent = notesOpen ? "Hide notes" : "Show notes";
    render();
  });

  const byPlatform = master.entries.reduce((acc, e) => {
    acc[e.platform] = (acc[e.platform] || 0) + 1;
    return acc;
  }, {});
  const flagged = master.entries.filter((e) => e.irregularity).length;
  const updated = master.meta && master.meta.last_updated ? master.meta.last_updated : "";
  statsEl.textContent =
    master.entries.length + " sourced entries" +
    (updated ? " · updated " + updated : "") +
    " · " + Object.entries(byPlatform).map(([k, v]) => v + " " + k).join(" · ") +
    " · " + flagged + " flagged for review";

  document.getElementById("flag-summary").innerHTML = master.entries
    .filter((e) => e.irregularity)
    .map((e) =>
      `<li><strong>${esc(e.platform)} ${esc(e.handle)}</strong> — ${esc(e.irregularity)} (${extLink(e.source_url, "source")})</li>`
    ).join("");

  const sources = (master.meta && master.meta.primary_sources) || [];
  document.getElementById("source-list").innerHTML = sources.map((s) =>
    `<li>${extLink(s.url, s.name)}${s.note ? " — " + esc(s.note) : ""}</li>`
  ).join("") || "<li>Source list missing from data/master-list.json.</li>";

  document.getElementById("meta-limits").innerHTML = (master.meta.limitations || [])
    .map((t) => `<li>${esc(t)}</li>`).join("");

  document.getElementById("strategy-disclaimer").textContent = strat.disclaimer || "";
  document.getElementById("official").innerHTML = (strat.official_resources || []).map((o) =>
    `<article class="card"><strong>${extLink(o.url, o.name)}</strong><p>${esc(o.why)}</p></article>`
  ).join("");

  const tactics = strat.official_tactics || [];
  document.getElementById("tactics").innerHTML = tactics.map((block) => `
    <h3>What the official page actually says</h3>
    <p class="note">Paraphrased from ${extLink(block.source_url, block.source_name)}, fetched ${esc(block.fetched)}. Not a guarantee, and not permission to buy engagement.</p>
    <ol class="tactic-list">${(block.points || []).map((p) => `<li>${esc(p)}</li>`).join("")}</ol>
  `).join("");

  document.getElementById("patterns").innerHTML = (strat.observed_patterns || []).map((p) =>
    `<li><strong>${esc(p.pattern)}.</strong> ${esc(p.example)}. ${esc(p.note)}</li>`
  ).join("");
  document.getElementById("topics").innerHTML = (strat.topics_with_public_demand || [])
    .map((t) => `<li>${esc(t)}</li>`).join("");

  document.getElementById("clocks-list").innerHTML = (strat.cited_clocks || []).map((c) => `
    <article class="card">
      <h3>${esc(c.account)}</h3>
      <p>${esc(c.clock)}</p>
      <p>${extLink(c.source_url, "Source")}</p>
      <p>${esc(c.caveat || "")}</p>
    </article>
  `).join("") || "<p class=\"note\">No cited clocks in this file.</p>";

  const likeRows = master.entries
    .filter((e) => e.platform === "TikTok")
    .map((e) => ({ e, ratio: likesPerFollower(e) }))
    .filter((x) => x.ratio != null)
    .sort((a, b) => b.ratio - a.ratio);
  document.getElementById("likes-rows").innerHTML = likeRows.map(({ e, ratio }) => `
    <tr>
      <td>${esc(e.handle)}</td>
      <td>${esc(fmt(e.metric_value))}</td>
      <td>${esc(e.likes_billions)}</td>
      <td>${esc(fmt(Math.round(ratio * 10) / 10))}</td>
      <td>${esc(e.cohort || "—")}</td>
    </tr>
  `).join("") || "<tr><td colspan=\"5\">No TikTok likes figures in this file.</td></tr>";

  const groups = new Map();
  for (const e of master.entries) {
    const key = e.platform + "\0" + (e.cohort || "—");
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(e);
  }
  const cohortRows = [...groups.entries()].sort((a, b) => a[0].localeCompare(b[0]));
  document.getElementById("cohort-rows").innerHTML = cohortRows.map(([, list]) => {
    const vals = list.map((e) => e.metric_value);
    const sample = list[0];
    return `<tr>
      <td>${esc(sample.platform)}</td>
      <td>${esc(sample.cohort || "—")}</td>
      <td>${esc(list.length)}</td>
      <td>${esc(fmt(median(vals)))}</td>
      <td>${esc(fmt(Math.min(...vals)))}</td>
      <td>${esc(fmt(Math.max(...vals)))}</td>
    </tr>`;
  }).join("");

  render();
}

load().catch((err) => {
  const count = document.getElementById("count");
  if (count) count.textContent = "Could not load data files. Open this page via GitHub Pages or a local server, not as a raw file.";
  console.error(err);
});
