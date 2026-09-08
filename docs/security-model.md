# Security model

## Public narrative

The important security property is the separation between transaction construction and signing. A client-controlled signer remains responsible for authorizing a transaction; the API is not presented as a wallet or custody service.

The case study should discuss, at a high level:

- input validation and bounded request handling;
- authentication and rate/policy controls;
- simulation and result checking where applicable;
- replay, expiry and idempotency considerations;
- provider and stream failure handling;
- structured logging that avoids secrets and sensitive wallet data;
- explicit trust assumptions and known limitations.

## Exclusions

Do not include key-management implementation, exact transaction-builder logic, RPC routing, production policy thresholds, live endpoints, credentials, wallet addresses, or claims that the system has been independently audited.
