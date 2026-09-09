# SolTrenchAPI — engineering case study

SolTrenchAPI is a case study of a private Solana API platform for realtime blockchain data and non-custodial transaction workflows. The production implementation remains private. This repository explains the engineering problem, system boundaries and validation approach without releasing the implementation.

## What the case study covers

- FastAPI/Python service design
- realtime data delivered through WebSockets
- unsigned transaction construction followed by explicit local signing
- simulation and broadcast boundaries
- provider failure handling and observability
- tests, QA and benchmark evidence

Public examples use local or Solana devnet data and do not connect to production systems. They contain no credentials.

## Review path

This repository is intentionally documentation-first. The runnable product
surface is the [SolTrench closed-beta site](https://soltrench.io/); this repo is
the sanitized engineering companion for a prospect or reviewer. A quick review
path is:

1. Read the [architecture note](docs/architecture.md) and [security model](docs/security-model.md).
2. Check the [benchmark methodology](docs/benchmarks.md) and
   [testing/reliability notes](docs/testing-reliability.md).
3. Browse the [redacted product screenshots](screenshots/).

The screenshots and written evidence are illustrative and do not represent a
production credential, endpoint, or private deployment detail.

## Architecture

The public architecture is intentionally high-level:

`Client → authenticated API boundary → validation/build layer → simulation boundary → client-controlled signing → optional broadcast`

The repository does not publish production endpoints, RPC routing, deployment topology, transaction-building internals or trading logic. The accompanying architecture and security notes define the reviewable abstraction.

## Evidence policy

Benchmarks are reported only with their measured operation, environment, sample size and limitations. A result from one path or environment is not presented as a general system latency claim.

## Public/private boundary

This is a portfolio explanation, not an open-source release of SolTrenchAPI. The production source, operational scripts, credentials, private infrastructure and commercially valuable algorithms remain private.
