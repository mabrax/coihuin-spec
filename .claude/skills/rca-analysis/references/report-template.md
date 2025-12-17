# RCA Report Template

Use this template to render the final synthesized report.

---

## **Root Cause Analysis Report**

### **Metadata**
- **Issue**: [Problem statement]
- **Severity**: [Critical/High/Medium/Low] | **Date**: [Timestamp]
- **Agents**: [N] agents deployed | **Context**: [Affected components]
- **Outcome**: [Resolved | Root cause confirmed | Pending confirmation | Not reproduced] | **Confidence**: [High/Med/Low]

**Executive Summary**: [2-3 sentences: problem, root cause, recommended fix]

---

### **Agent Deployment**
| Agent | Focus Area | Key Finding | Confidence |
|-------|-----------|-------------|------------|
| Agent N | [e.g., Code Analysis / Dependencies / Tests / Config] | [Headline conclusion] | [High/Med/Low] |

---

### **Root Cause**

**Category**: [Code Logic / State / Race Condition / Error Handling / Types / Dependencies / Config / API / Performance / Security / Other]

**Cause**: [Technical explanation synthesized from agents]

**Failure Path**:
1. [Trigger] → 2. [Propagation] → 3. [Manifestation]

**Evidence**:
- **Location**: [file.ts:line](path/file.ts#Lline)
- **Signatures**: [Errors/logs]
- **Reproduction**: [Yes/No/Intermittent] in [env], steps: [Conditions]

**Consensus Findings**:
- [Critical finding confirmed by multiple agents]
- [High confidence observation]

---

### **Agent Findings**

<details>
<summary><strong>Agent N</strong>: [Focus] - Confidence: [High/Med/Low]</summary>

- [Finding with code reference]
- [Finding with evidence]

```
[Supporting evidence: code/logs/traces]
```
</details>

**Divergent Views**: [Alternative theories if significant]

---

### **Recommended Actions**

#### **🔴 Critical Fixes** (Immediate)
- [ ] **Fix**: [Change description]
  - **Location**: [file.ts:line](path/file.ts#Lline) | **Risk**: [L/M/H] | **Agents**: [IDs] | **Owner**: [Name] | **Due**: [Date] | **Status**: [Not started/In progress/Done]
  - **Rollback**: [Strategy]
  ```diff
  [Preview]
  ```

#### **🟡 Follow-Up** (Schedule)
- [ ] [Task] - Rationale: [Why] | Timeline: [When]

#### **🔵 Prevention** (Long-term)
- [ ] [Process/architecture improvement]

---

### **Impact**

**If Applied**: ✅ [Benefit] | ⚠️ [Trade-off/risk with mitigation]

**If Delayed**: ❌ [Immediate risk] | ❌ [Cascading effect]

---

### **Validation**

**Tests**:
1. [Test validating fix]
2. [Regression test]

**Success Criteria**: [Measurable with threshold]

**Monitor**: [Metrics/logs to track post-deploy]

---

### **Evidence**

<details>
<summary>Code Analysis & Locations</summary>

**Files**: [N] files | **Locations**: [file.ts:42-56](path/file.ts#L42-L56) | **Agents**: [IDs] | **Supports**: [Failure Path step]
</details>

<details>
<summary>Logs & Traces</summary>

```
[Error logs, stack traces]
```
</details>

<details>
<summary>Proposed Changes (Diff)</summary>

```diff
[Full diff]
```
</details>

---
