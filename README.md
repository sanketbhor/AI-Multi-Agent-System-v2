# AI-Multi-Agent-System-

-What you'll build

User
   │
   ▼
Planner
   │
   ▼
Research Agent
   │
   ▼
Critic Agent
   │
   ├───────────────┐
   │               │
   ▼               │
Good?              │
   │               │
 Yes               │ No
   │               │
   ▼               │
Answer Agent ◄─────┘

This introduces:

✅ Agent collaboration
✅ Agent feedback loop
✅ Conditional routing
✅ Self-improving answers

This is much closer to production AI systems.


1] Planner Agent Understand the user's request. Decide which agents are required. Store the plan in the state.

2] Research Agent Uses DuckDuckGo
Wikipedia
Calculator
Datetime

3]Critic Agent The critic checks whether the research result is good enough..

4]Answer Agent

This agent receives:

User question
Research results
Calculator results and produces the final answer.