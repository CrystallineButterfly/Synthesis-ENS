"""Project-specific context for NameMesh Control Plane."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "NameMesh Control Plane",
    "track": "ENS",
    "pitch": "An ENS-native control plane that lets agents coordinate, route payments, and emit human-readable receipts without falling back to raw addresses.",
    "overlap_targets": [
        "Venice Private Agents",
        "PayWithLocus",
        "MetaMask Delegations",
        "ERC-8004 Receipts",
        "Slice",
        "YieldGuard"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
