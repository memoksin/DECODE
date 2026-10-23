---
name: diagramming
description: Diagram rules from CNG350/CNG351 for SRS/SDD work. Use when drawing or reviewing a context diagram, use case diagram, ERD/EER, class, sequence, activity, DFD, state or component diagram.
---

# Diagramming rules

Sources: CNG350 lectures/solutions/rubric, CNG351 notes. Keep diagrams simple, labels short.

## General
- PlantUML for everything except ERD (Chen, draw.io).
- Unreadable diagram = not graded. Same style across the report.
- Few elements, left-to-right, no crossing lines where avoidable.

## Context diagram (SRS 1.4.1)
- System box in the centre, only EXTERNAL systems around it.
- Plain lines, no arrowheads. No actors, no database.
- External systems may carry `«system»`.
- One diagram + 3 bullets. Max 2 interfaces.
- 2.1 table must match: System Interface | Functionality | Input | Output.

## Use case diagram (SRS 2.2)
- Actors outside the system boundary box, use cases inside. Draw the boundary.
- Actor to use case: plain line, no arrow. External system = actor.
- `include`: dashed arrow base -> included (always runs).
- `extend`: dashed arrow extension -> base (optional).
- Generalization: hollow triangle, specific -> general.
- Name = verb + noun, unique. No UI steps ("Click Submit"). No link between unrelated use cases.
- Include/extend used by one base: describe inside the base. Shared by many: describe separately.
- Abstract parent use cases are not described.

## ERD / EER (SRS 2.5) — Chen notation, draw.io
- Other notations get zero in CNG351.
- Entity: rectangle. Attribute: oval. Key: underlined. Multivalued: double oval. Composite: sub-ovals.
- Relationship: diamond. Mark 1:1 / 1:N / M:N on edges.
- Participation: double line = total, single line = partial.
- Every relationship shows cardinality AND participation.
- Recursive relationship: role names. Relationship attributes on the diamond.
- Weak entity: partial key + identifying relationship to owner.
- Avoid ternary relationships. Write assumptions explicitly.
- EER: `d`/`o` for disjoint/overlapping, double/single line for total/partial.
- Add entity table: Entity | Purpose | Attributes | Relationships.

## Class diagram (SDD)
- Attributes private (`-`), methods public (`+`), with parameters. Skip trivial getters/setters.
- `name : Type`, `name(p : Type) : Ret`.
- Every "has a list of X" needs the attribute AND an association line.
- Multiplicity on both ends. Association type shown.
- Composition (filled diamond on whole): part dies with whole. Aggregation (hollow): part independent.
- Generalization: hollow triangle at the superclass.
- Keep external systems out. No "Unregistered User" class.
- Add a short design rationale under the diagram.

## Sequence diagram (SDD)
- Lifelines left to right: Actor -> Screen -> Controller -> Domain class -> DB. Controller and DB are required (marks were lost without them).
- Return messages dashed. Use `alt` / `opt` / `loop` with `[guard]`. Show failure branches.
- Message names = methods of the receiving class in the class diagram.
- OO variant: only classes as participants, every message is a class method.

## Activity diagram
- One start, one end. Decision diamond with guards for exclusive paths. Fork/join only for true concurrency.
- Swimlanes only for actor perspective. No join after a merge.

## DFD
- Process: verb phrase, numbered (1.0). Flows and stores: noun phrases, no verbs.
- Flow to/from a store goes through a process. No entity-to-entity flow. No self-loop. Bidirectional = two arrows.
- Context DFD: one process, no stores. Level n keeps parent flows (balancing); sub-processes use parent number prefix (4.1).

## State chart
- Initial dot, final ringed dot, events and guards on transitions. Add a state table if the diagram is large.

## Component / deployment
- Component: ball = provided, socket = required interface.
- Deployment: nodes as boxes, `«device»`, connection labelled with protocol.
