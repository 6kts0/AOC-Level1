# Advent of Code 2025 - Level One Submission

## Progress

**Part One: Complete** - Password: `1089`
  - Count the number of times the dial lands on 0 after any rotation

**Part Two: In-progress**
  - count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

## Problem Summary

A safe dial (0-99) starts at position 50. Given a sequence of rotations (`L`/`R` with distance), calculate how many times it points at 0.

| Part | Task | Answer |
|------|------|--------|
| One | Count landings on 0 after each rotation | 1089 |

## Key Challenge

- **Wraparound logic**: Left from 0 goes to 99, right from 99 goes to 0
- **Intermediate counting**: Track every position during a rotation, not just the endpoint
- **Large rotations**: Handle cases where a single rotation passes through 0 multiple times
