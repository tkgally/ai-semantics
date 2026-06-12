# Cloud-compute feasibility / scoping note

> **HISTORICAL RECORD (annotated 2026-06-12).** This note's operative assumption — that Tom
> might provision a `TOGETHER_API_KEY` — is superseded by the pure-autonomy ruling
> (`wiki/decisions/resolved/autonomous-era-governance.md`, Ruling 3), and its "$20/week" budget
> framing is superseded by the **$5.00/day (UTC)** cap. Both governing decisions are resolved:
> `wiki/decisions/resolved/cloud-compute-path.md` (RETIRED/CLOSED) and
> `wiki/decisions/resolved/aann-panel-logprob-blocker.md` (logprob path terminated; behavioral
> re-operationalization opened). The capability/pricing tables below are dated 2026-05-31
> snapshots — re-verify before any hypothetical future use.

**Status:** scoping only (Tom decision 5, this round). **No rebuild committed.** This note
reports what is *actually* possible for the two capabilities OpenRouter cannot provide,
within (a) this environment's network policy and (b) the newly-raised **$20/week soft**
budget. It does **not** run anything or change the panel. All prices/capabilities below
carry a URL + access date; anything I could not verify is marked **UNVERIFIED**.

The two blocked capabilities (from
[`decisions/resolved/aann-panel-logprob-blocker`](../../wiki/decisions/resolved/aann-panel-logprob-blocker.md)):

- **CAP-1 — provided-string surprisal.** Per-token log-probability / surprisal of a
  *specific provided continuation string* (echo / prompt-logprobs semantics). This is the
  AANN **Option-A** indicator: score the licit AANN string vs. four degenerate variants by
  the summed per-token surprisal of each *given* string. OpenRouter exposes no echo /
  prompt-logprobs on any panel model, so CAP-1 is uncomputable there. (Top-k logprobs of
  *generated* tokens — which some OpenRouter models do expose — is **not** CAP-1: it scores
  what the model *chose*, not the surprisal of a string *you* supply.)
- **CAP-2 — model-internal representations.** Hidden states / layer activations / token
  embeddings for the deferred "small-model representation lanes" (both the grammatical and
  the lexical axes).

---

## 0. This environment's network + local stack (measured 2026-05-31)

Measured from inside this agent's sandbox with `curl` / `env` / `python3`:

| Probe | Result |
|---|---|
| `huggingface.co`, `huggingface.co/api/models` | **200** (reachable) |
| `api-inference.huggingface.co` (legacy serverless) | **000** (no egress / blocked) |
| `router.huggingface.co/v1/chat/completions` (new Inference Providers host) | **401** (reachable; auth-gated) |
| `api.endpoints.huggingface.cloud` (dedicated-Endpoints control plane) | **200** (reachable) |
| `api.together.xyz/v1/completions` with `echo:true, logprobs:1` body | **HTTP 401 "Missing API key"** — reachable; the request *body was accepted*, only the key was missing |
| `api.replicate.com/v1/models` | **401** (reachable; auth-gated) |
| `api.fireworks.ai` / `api.openai.com` | 404 / 421 (host resolves; reachable) |
| `colab.research.google.com`, `kaggle.com` | **200** (landing pages only — not proof of programmatic drive) |
| Local GPU (`nvidia-smi`) | **none** |
| Local `torch` / `transformers` | **not installed** |
| API keys in env | **only `OPENROUTER_API_KEY`** (+ `GITHUB_TOKEN`). No HF / Together / Replicate / Google / Kaggle key present. |

Two load-bearing consequences:

1. **No local compute.** This sandbox has no GPU and no ML stack, so "run a small HF model
   locally *in this agent*" is out — every option below is a remote service.
2. **Every remote service that could do CAP-1/CAP-2 needs an API key this environment does
   not have.** So even where the *host* is reachable and the *capability* exists, **this
   headless agent cannot drive it without Tom provisioning a key** (a `*_API_KEY` env var or
   a written-in secret). That is the central operational gate, separate from the budget.

---

## 1. Verdict table — capability × platform

Legend: **YES** = capability verified to exist; **NO** = verified absent; **UNVERIFIED** =
could not confirm. "Headless-drivable here?" = could *this* agent run it given a key, vs.
needs Tom out-of-band.

### CAP-1 — provided-string surprisal (the AANN Option-A blocker)

| Platform | CAP-1 supported? | How | Cost | Headless-drivable here? |
|---|---|---|---|---|
| **Together AI `/v1/completions`** | **YES** (documented) | `echo=true` + `logprobs` → response carries a `prompt` block with `token_logprobs` for the *echoed prompt* tokens (first token `None`, no prior context) | tiny: small open models **$0.06–0.15 /M tokens** (Gemma 3n E4B $0.06/$0.12; Llama-3-8B-Lite $0.10/$0.10) — an AANN run is far under **$1** | **YES, IF Tom adds `TOGETHER_API_KEY`.** Host reachable from here; body already accepted (401 was key-only). |
| **Fireworks AI `/completions`** | **YES** (documented) | `echo=true` returns prompt; `logprobs` returns per-token logprobs incl. "how the model tokenized your input"; experimental `raw_output` exposes `prompt_token_ids` | small-model serverless; not priced here (**UNVERIFIED $**) | **YES, IF** Tom adds a Fireworks key (host reachable). |
| **Self-hosted vLLM (OpenAI-compatible)** e.g. on an HF Endpoint / Modal / Replicate-Cog | **YES** (documented) | `prompt_logprobs` param (vLLM extension) or `echo=True`+`logprobs=1` → per-prompt-token logprobs; known rough edges in older builds (vLLM issues #5264/#5334) | GPU-hour (see CAP-2 table) | Drivable **only after** Tom stands up the server + key; the *standing-up* is out-of-band. |
| **HF local `transformers` on an Endpoint / Colab / Kaggle** | **YES** (surest) | `model(input_ids).logits` → log-softmax → gather the provided continuation's token logprobs directly. The cleanest, most exact CAP-1; no API ambiguity. | GPU-hour or free (see CAP-2) | **Colab/Kaggle = NO for this agent** (interactive / human session — Tom out-of-band). **HF Endpoint custom handler = YES if Tom provisions** the endpoint + key. |
| **HF Inference Providers** (`router.huggingface.co`, serverless) | **UNVERIFIED / likely NO for CAP-1** | exposes `logprobs`/`top_logprobs` for *generated* tokens (chat), but echo/prompt-logprobs is **provider-dependent** and the legacy feature request for prompt-logprobs was never generally shipped | per-token, provider-set | host reachable; but CAP-1 itself unconfirmed → do not rely on it |
| **HF legacy serverless** (`api-inference.huggingface.co`) | n/a | — | — | **NO — host returns 000 (blocked) from this sandbox** regardless of capability |
| **OpenRouter (current panel)** | **NO** (re-verified in the blocker decision) | no echo / prompt-logprobs on any panel or candidate model | — | n/a |

### CAP-2 — hidden states / internal representations (small-model representation lanes)

| Platform | CAP-2 supported? | How | Cost | Headless-drivable here? |
|---|---|---|---|---|
| **HF local `transformers`** on a GPU (Endpoint custom handler, Colab, or Kaggle) | **YES** (surest) | `output_hidden_states=True` / `output_scores=True` (documented) returns every layer's hidden states + per-step scores | GPU-hour or free | **Endpoint = YES if Tom provisions**; Colab/Kaggle = Tom out-of-band |
| **HF Inference Endpoints (dedicated)** | **YES** via a custom handler returning hidden states; the GPU runs your own `transformers` code | **T4 $0.50/hr**, L4 $0.70–0.80, A10G $1.00, A100 $2.50–3.60; billed **per minute**; **no documented scale-to-zero** (min 1 replica → idle still bills) | control-plane host reachable; needs Tom's account + key + (manual) endpoint creation |
| **Modal** | **YES** (run arbitrary `transformers` w/ GPU; serverless, scales to zero) | your own code → hidden states | GPU/sec, scale-to-zero (exact rate **UNVERIFIED** this run); free monthly credit historically offered (**UNVERIFIED amount**) | host reachable; needs Tom's account + token; deploy is a one-time out-of-band setup, then API-drivable |
| **Replicate (custom Cog model)** | **YES** *if you build a Cog model that returns them* | package `transformers` in Cog, output hidden states in the schema | GPU/sec billing (**UNVERIFIED rate**) | host reachable; building+pushing the Cog model is out-of-band, then API-drivable with a key |
| **Serverless chat APIs** (Together / Fireworks / OpenRouter / HF Providers) | **NO** | no chat/completions API returns hidden states; vLLM RFCs (#18176, #24288) to expose them are open, not shipped | — | n/a |

### Free GPU notebooks (relevant to both CAPs)

| Platform | Can extract CAP-1 + CAP-2? | Limits / cost | Headless-drivable by THIS agent? |
|---|---|---|---|
| **Google Colab (free)** | **YES** (local `transformers` on the T4 — full logprobs + hidden states) | free T4, 12 h max session / 90 min idle, GPU not guaranteed at peak; Pro $9.99–11.99/mo (CU model; T4 ≈1.76 CU/hr); Pro+ $49.99/mo adds background exec | **NO — interactive, human-driven.** Tom runs it out-of-band. Not headlessly drivable from this sandbox. |
| **Kaggle Notebooks** | **YES** (same: local `transformers`, T4/P100) | **~30 GPU-hr/week free** ("floating" quota); internet-enabled kernels | **PARTIAL / borderline.** Kaggle has a real **Kernels push/run API** (`kaggle kernels push`, metadata JSON, `enable_gpu`/`enable_internet`) used for CI/CD — so it is *programmatically* drivable in principle. BUT: kaggle CLI not installed here, no Kaggle key in env, and it is asynchronous batch (push → poll → pull output). Realistically **Tom out-of-band**, though a future session *could* script it if Tom adds a `kaggle.json`/key. |

---

## 2. Headline — is there a real path?

**Yes for CAP-1, conditional on one key. The cleanest CAP-1 path that this headless agent
could actually drive is Together AI `/v1/completions` with `echo=true, logprobs=1`,**
which returns per-token logprobs over the *provided* (echoed) prompt string — exactly the
AANN Option-A indicator — on a cheap small open model (Gemma/Llama-8B, **<$1** for the whole
probe, trivially inside $20/week). The host is reachable from this sandbox and already
accepted the request body; the **only** thing missing is a `TOGETHER_API_KEY`. Fireworks is
an equivalent fallback. Caveat: this is *one* model, not a decorrelated panel — it realizes
the **ratified Option-A surprisal indicator** but as a single open-weight subject (which is
exactly the blocker decision's "Option B / small-model lane", now shown to be cheap and,
crucially, *API-drivable* rather than requiring local GPU).

**Yes for CAP-2, but not headlessly by this agent without setup.** Hidden states require
running `transformers`/`vLLM` *code you control* on a GPU — no serverless chat API returns
them. The reachable, in-budget routes are: an **HF dedicated Endpoint** with a custom
handler (**T4 $0.50/hr**, per-minute billing → a representation-extraction job over a few
hundred items is well under $20/week if torn down promptly, but **no scale-to-zero** means
idle time bills, so it must be created→run→deleted), **Modal** (scale-to-zero, exact rate
unverified), or a free **Colab/Kaggle** notebook. All of these need either Tom's account/key
or are interactive — **none is drivable end-to-end by this autonomous agent today**, and
the Endpoint/Modal/Cog setup is a one-time out-of-band step before any API drive.

**The honest distinction this note adds to the blocker decision:** the blocker page assumed
the small-model lane "needs local compute stood up." That is true for CAP-2 (hidden states),
but **CAP-1 (the AANN Option-A surprisal) does *not* need local compute** — a serverless
`echo+logprobs` completions API (Together/Fireworks) delivers it for cents, and one of them
is reachable from here. The only true blocker for CAP-1 is a **single API key**, not compute.

---

## 3. Recommended decision (for the orchestrator to surface — I did not create it)

**Suggested id:** `cloud-compute-path`
**Type:** open decision (operationalization / instrument + a small spend authorization).
**Question:** Do we open a cloud-compute path for the two OpenRouter-blocked capabilities,
and if so which, given it requires Tom to provision an API key/account?

**Options:**

- **Option A (provisional default) — open CAP-1 only, via Together `echo+logprobs`.**
  Tom adds a `TOGETHER_API_KEY` (free signup; small-model spend <$1/probe, inside $20/wk).
  A future session runs the **AANN Option-A surprisal indicator** on one small open-weight
  model (e.g. Llama-3-8B or Gemma) — the *exact* ratified primary indicator the OpenRouter
  panel cannot compute. This is the smallest, cheapest, most reversible step and it
  **unblocks the AANN probe** (as a single-model surprisal subject, not a panel — note this
  in the result: no cross-family signal). Leaves CAP-2 deferred.
  - *Why default:* lowest cost, lowest setup, directly cashes out the ratified Option-A
    indicator that has been on hold; one key is the whole ask. It does **not** pre-judge
    whether AANN comes out positive or null — it only restores the yardstick.
  - *Integrity note:* a single open model is a different evidential profile from the
    decorrelated panel; the AANN result must be reported as single-model surprisal, and the
    panel/decorrelation question for AANN stays as the blocker decision frames it.

- **Option B — open CAP-1 *and* CAP-2 via an HF dedicated Endpoint (T4 $0.50/hr) or Modal.**
  Tom provisions the account/key; a future session (or Tom) stands up a custom-handler
  endpoint that returns both per-token logprobs (CAP-1) and hidden states (CAP-2), enabling
  the AANN surprisal probe *and* the deferred representation lanes (grammatical + lexical).
  - *Pro:* opens everything; reusable for every future surprisal/representation probe.
  - *Con:* more setup + ongoing care (no scale-to-zero on HF Endpoints → must create/run/
    delete each session to stay in budget); CAP-2 lanes are still design-stage, so this buys
    capability ahead of a ratified representation design.

- **Option C — keep both deferred (no new platform, no key).** Status quo: AANN stays on
  hold, representation lanes stay deferred, as currently stated. First-class and honest if
  Tom does not want to add a key / manage spend on a second platform right now.
  - *Pro:* zero new surface, zero new spend, no second budget to track.
  - *Con:* the AANN primary indicator stays uncomputed even though a cheap path now exists.

**My recommendation:** surface all three; **provisional default = Option A** — it is the
minimal move that converts a standing blocker ("needs local compute") into a one-key task,
costs cents, and realizes the *ratified* indicator rather than a degraded fallback. CAP-2
(Option B) is worth doing but should wait for a ratified representation-lane *design*, so it
need not be bundled with the AANN unblock.

**This is value-laden (it changes how/whether AANN is measured and adds a platform + spend),
so it is surfaced, not auto-resolved.** One line from Tom suffices: "add a Together key, run
AANN Option-A single-model" (A) / "stand up an HF Endpoint for both" (B) / "keep deferred" (C).

---

## 4. Unverified claims left open (do not treat as settled)

- **Fireworks small-model pricing** — not priced this run (capability YES, $ UNVERIFIED).
- **Modal GPU/sec rate and free-credit amount** — UNVERIFIED (capability YES; scale-to-zero
  is a documented Modal feature but the exact rate was not fetched this run).
- **Replicate per-second GPU rate** — UNVERIFIED (custom-Cog path for CAP-2 is sound in
  principle but the price was not pinned).
- **HF Inference Providers (router) CAP-1** — UNVERIFIED whether *any* current provider behind
  the router returns echo/prompt-logprobs; treat as likely-NO until confirmed.
- **Together free-tier / new-account credits** — pricing page did not disclose; signup-flow
  credits UNVERIFIED (the per-token rates above are the conservative basis, and they are
  already trivially in-budget).
- **Together `echo+logprobs` end-to-end on a *named* current model** — the schema and docs
  confirm CAP-1; a *live* call confirming a specific 2026 model still returns
  `prompt.token_logprobs` was **not made** (no key, and no spend authorized). The 401 proves
  reachability + body acceptance, not the returned-field contents. Confirm on first real use.
- **Kaggle Kernels API as a fully headless driver from a future session** — the push/run API
  exists and is used for CI/CD, but I did not exercise it (no CLI/key here); feasibility for
  an autonomous session is plausible-but-UNVERIFIED.

---

## Provenance (accessed 2026-05-31)

- HF Inference Providers / logprobs & top_logprobs (generated tokens; echo provider-dependent):
  <https://huggingface.co/docs/inference-providers/en/index> ·
  <https://huggingface.co/docs/inference-providers/en/tasks/chat-completion> ·
  prompt-logprobs feature request never generally shipped:
  <https://github.com/huggingface/text-generation-inference/issues/1069>
- HF Inference Endpoints GPU pricing (T4 $0.50/hr, L4, A10G, A100; per-minute billing; min-1-replica):
  <https://huggingface.co/docs/inference-endpoints/en/pricing>
- HF `transformers` hidden states / scores (`output_hidden_states`, `output_scores`):
  <https://huggingface.co/docs/inference-providers/en/index> (clients) ·
  <https://discuss.huggingface.co/t/the-hidden-states-when-i-use-model-generate/73169>
- Together `/completions` echo + prompt logprobs (`token_ids`/`tokens`/`token_logprobs`, first token `None`):
  <https://docs.together.ai/reference/completions-1> · <https://docs.together.ai/docs/logprobs>
- Together small-model pricing (Gemma 3n E4B $0.06/$0.12; Llama-3-8B-Lite $0.10/$0.10; Qwen3.5 9B $0.10/$0.15):
  <https://www.together.ai/pricing>
- Fireworks echo + logprobs + `raw_output.prompt_token_ids`:
  <https://docs.fireworks.ai/guides/querying-text-models>
- vLLM `prompt_logprobs` / `echo=True`+`logprobs=1` (OpenAI-compatible server; known edge cases):
  <https://github.com/vllm-project/vllm/issues/6508> · <https://github.com/vllm-project/vllm/issues/5264> ·
  <https://github.com/vllm-project/vllm/issues/5334> · hidden-states RFCs (not shipped):
  <https://github.com/vllm-project/vllm/issues/18176> · <https://github.com/vllm-project/vllm/issues/24288>
- Replicate custom Cog models (control over output schema):
  <https://replicate.com/docs/guides/build/push-a-model>
- Google Colab limits/pricing (free T4, 12 h/90 min idle; Pro $9.99–11.99; Pro+ $49.99; CU model):
  <https://colab.research.google.com/signup> · <https://research.google.com/colaboratory/faq.html>
- Kaggle ~30 GPU-hr/week + Kernels push/run API (headless CI/CD):
  <https://www.kaggle.com/product-feedback/173129> · <https://www.kaggle.com/docs/api> ·
  <https://github.com/Kaggle/kaggle-cli>
- Network/stack measurements: `curl`/`env`/`python3` from this sandbox, 2026-05-31 (see §0).
