"""Smoke: HF domain charter stream schema for research-health-bio."""

from __future__ import annotations

from datasets import load_dataset


def test_emotion_stream_schema() -> None:
    rows = list(
        load_dataset("dair-ai/emotion", "split", split="train", streaming=True).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "label" in r and "text" in r
