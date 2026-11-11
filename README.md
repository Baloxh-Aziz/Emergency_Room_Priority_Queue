# 🏥 Emergency Room Priority Queue

A priority-queue simulation of an Emergency Room that treats patients based
on severity rather than arrival order, with capacity limits and an
emergency-override rule for critical cases.

## 📋 Overview

This project models a hospital ER using a priority queue data structure:

1. **Patient** — a simple class holding a patient's name and severity level (lower number = higher priority/more critical)
2. **EmergencyRoom** — manages a capacity-limited queue of patients, always kept sorted by severity
3. **Capacity Handling** — once the queue is full, new (non-critical) patients are rejected
4. **Emergency Override** — a severity-0 (most critical) patient is force-added even when the queue is full, bypassing the capacity limit
5. **Treatment** — the most critical patient is always treated first (queue behaves as a priority queue, not FIFO)

## ⚙️ How It Works

| Method            | Behavior                                                                 |
| ------------------ | ------------------------------------------------------------------------- |
| `add_patient()`    | Adds a patient and re-sorts the queue by severity; rejects new patients if full, unless the patient is severity 0 (emergency override) |
| `treat_patient()`  | Removes and treats the patient with the lowest severity number (highest priority) |
| `show_queue()`     | Prints the current queue in priority order                               |

- Default capacity: **6** patients
- Priority rule: **lower severity number = treated first**

## 📈 Example Run

```python
er = EmergencyRoom()
er.add_patient(Patient("Zara", 2))
er.add_patient(Patient("Ali", 5))
er.add_patient(Patient("Fatima", 3))
er.add_patient(Patient("John", 1))
er.show_queue()
er.treat_patient()
er.show_queue()
```

**Output:**

```
Current Patient Queue:
1. John (Severity: 1)
2. Zara (Severity: 2)
3. Fatima (Severity: 3)
4. Ali (Severity: 5)

Treating: John (Severity: 1)

Current Patient Queue:
1. Zara (Severity: 2)
2. Fatima (Severity: 3)
3. Ali (Severity: 5)
```

Even though patients were added in the order Zara → Ali → Fatima → John,
the queue always stays sorted by severity, so John (severity 1) is treated
first.

## 🛠️ Tech Stack

- **Python 3** (no external dependencies — uses only built-in list sorting)

## 🚀 Possible Extensions

- Replace the list + `sort()` approach with Python's `heapq` for a true O(log n) priority queue
- Add timestamps so equally-severe patients are treated in arrival order (stable tie-breaking)
- Add a waiting-time tracker to flag patients who've waited too long
