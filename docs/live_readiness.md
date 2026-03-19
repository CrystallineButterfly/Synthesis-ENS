# Live readiness

- **Project:** NameMesh Control Plane
- **Track:** ENS
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:11+00:00`

## Trust boundaries

- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Slice** — `rest_json` — Drive checkout hooks and storefront policy changes.

## Offline-ready partner paths

- **ENS** — prepared_contract_call
- **MetaMask Delegations** — prepared_contract_call
- **ERC-8004 Receipts** — prepared_contract_call

## Live-only partner blockers

- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Slice**: SLICE_API_KEY, SLICE_HOOK_URL — https://docs.slice.so/

## Highest-sensitivity actions

- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.
- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for EnsCoordinationRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for ens_mesh.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
