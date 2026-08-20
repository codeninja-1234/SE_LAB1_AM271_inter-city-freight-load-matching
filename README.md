# Inter-City Freight Load Matching Marketplace

**PES University — Dept. of CSE**  
**Lab 1: Requirements Engineering & UML Use-Case Modelling**  
**Problem Statement #28: Smart Cities, Transport & Logistics**

## Project Overview

This repository contains the three required deliverables for the Inter-City Freight Load Matching Marketplace problem statement.

The system is a B2B freight brokerage exchange where commercial shippers post cargo loads, trucking carriers submit competitive bids, and milestone payments are released automatically after verified proof of delivery.

## Deliverables

1. **Requirements_Table.pdf**
   - Exactly 5 Functional Requirements: FR-001 to FR-005
   - 2 Non-Functional Requirements: NFR-001 and NFR-002
   - Includes ID, Type, Description, Priority, Acceptance Criteria, and Rationale

2. **Use_Case_Diagram.pdf**
   - UML use-case diagram
   - Actors: Shipper and Freight Carrier
   - Includes `«include»` and `«extend»` relationships

3. **Use_Case_Diagram.pdf**
   - UML use-case diagram with Shipper and Freight Carrier
   - Includes `«include»` and `«extend»` relationships

3. **Use_Case_Flow.pdf**
   - Core use case: Submit Competitive Bid
   - Preconditions
   - Postconditions
   - Main Success Scenario
   - One Alternate Flow

## Main Actors

- **Shipper** — posts freight shipments, reviews bids, selects carriers, and verifies delivery.
- **Freight Carrier** — browses loads, submits bids, tracks shipments, and submits proof of delivery.

## Key Use Cases

- Register / Verify Account
- Post Freight Shipment
- Browse Freight Loads
- Submit Bid
- View Bids
- Select Winning Carrier
- Track Shipment
- Submit Proof of Delivery
- Verify Proof of Delivery
- Release Escrow Payment

## UML Relationships

### Include
- Submit Bid `«include»` Verify Carrier Credentials
- Submit Proof of Delivery `«include»` Verify Proof of Delivery
- Verify Proof of Delivery `«include»` Release Escrow Payment

### Extend
- Submit Bid `«extend»` Browse Freight Loads

## Repository Structure

```text
Problem-28-Freight-Matching/
├── README.md
├── Requirements_Table.pdf
├── Use_Case_Diagram.pdf
└── Use_Case_Flow.pdf
```

## Submission

Upload all files to your GitHub repository and submit the repository link according to your lab instructions.

