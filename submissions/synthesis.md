# NameMesh Control Plane

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-ENS
- **Primary track:** ENS
- **Overlap targets:** Venice Private Agents, PayWithLocus, MetaMask Delegations, ERC-8004 Receipts, Slice, YieldGuard
- **Primary contract:** EnsCoordinationRegistry
- **Primary operator module:** ens_mesh
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

An ENS-native control plane that lets agents coordinate, route payments, and emit human-readable receipts without falling back to raw addresses.

## Track evidence

- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "NameMesh Control Plane",
  "track": "ENS",
  "plan_id": "0x69fd1de01c403c84be2fb3d12e5db6576682d64ca84b3424b9d43c5c25b25db2",
  "simulation_hash": "0xf1c9131e6ea108e706e76672667dc5aa14fcfaa79c9dfeec6fa0366e5a92a002",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/ens_ens_publish.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json",
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json"
  ],
  "partner_statuses": {
    "ENS": "prepared_contract_call",
    "Venice": "awaiting_credentials",
    "PayWithLocus": "awaiting_credentials",
    "MetaMask Delegations": "prepared_contract_call",
    "ERC-8004 Receipts": "prepared_contract_call",
    "Slice": "awaiting_credentials"
  },
  "created_at": "2026-03-19T03:52:11+00:00"
}
```
