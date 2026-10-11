"""Length-aware queue activation contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass

MOD_ID = "org.vllm-hust.stateaxis-length-aware-queue"


@dataclass(frozen=True, slots=True)
class LengthAwareQueueConfig:
    """Exact bounded cold-prefill length-class and aging contract."""

    enabled: bool = True
    telemetry_enabled: bool = True
    authority_enabled: bool = True
    scope: str = "cold-prefill-no-state"
    short_max_tokens: int = 128
    medium_max_tokens: int = 512
    aging_ms: int = 250
    max_queued_requests: int = 64
    max_queued_tokens: int = 1_048_576
    atomic_full_plan_reorder: bool = True
    trace_identity_aligned: bool = True
    stateful_or_decode_fallback: bool = True
    monotonic_clock_fail_closed: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        expected = {
            "enabled": True,
            "telemetry_enabled": True,
            "authority_enabled": True,
            "scope": "cold-prefill-no-state",
            "short_max_tokens": 128,
            "medium_max_tokens": 512,
            "aging_ms": 250,
            "max_queued_requests": 64,
            "max_queued_tokens": 1_048_576,
            "atomic_full_plan_reorder": True,
            "trace_identity_aligned": True,
            "stateful_or_decode_fallback": True,
            "monotonic_clock_fail_closed": True,
            "fail_closed": True,
        }
        if asdict(self) != expected:
            raise ValueError("length-aware queue requires the reviewed contract")


def length_aware_queue() -> LengthAwareQueueConfig:
    return LengthAwareQueueConfig()


__all__ = ["MOD_ID", "LengthAwareQueueConfig", "length_aware_queue"]
