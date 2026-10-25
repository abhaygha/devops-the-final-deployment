# DevOps: The Final Deployment — timed Hinglish screenplay

**Draft v1.0 | 25:00 total | 14 scenes**

The dialogue is a performance draft. Scene allocations include reaction comedy, screen action, silent gags, establishing shots, and music. Lock timings with an audio animatic.

## Scene 00 — Cold open: Production is on fire (1:30)

**Action:** Red alarms; Chintu announces cloud cost savings because everything is gone.

**Dialogue / beats:**
Manager: “WHO TOUCHED PRODUCTION?!”
Senior: “Sir, woh toh main bhi pooch raha hoon!”
Junior: “Sir, ek good news aur ek bad news.”
Manager: “Good news?”
Junior: “Cloud ka bill bahut kam ho jayega.”
Manager: “Bad news?”
Junior: “Cloud mein kuch bacha hi nahi.”
[Slow-motion falling coffee, freeze frame, narrator: “Six hours earlier...”]


## Scene 01 — Meet the DevOps legends (1:30)

**Action:** Mockumentary introductions, ETA montage and tutorial jokes.

**Dialogue / beats:**
Narrator introduces Mr. Deadline, Captain Jira, Baba Kubernetes and Chintu YAML.
Manager: “My job is leadership. By asking ETA.”
Lead: “Production down? Ticket. Coffee down? High priority ticket.”
Senior: “Kisi ne production touch kiya toh Himalaya chala jaunga.”
Junior: “Sir, Docker, Kubernetes, Terraform sab aata hai. Playlist double speed pe complete ki!”


## Scene 02 — The impossible deployment promise (2:00)

**Action:** Manager promises zero downtime and zero risk before lunch.

**Dialogue / beats:**
Executive: “Zero downtime, zero risk, zero cost. By lunch?”
Manager: “Absolutely!”
Senior: “Sir, testing complete nahi hui.”
Manager: “Client ke saamne negative mat bolo.”
Senior: “Deployment, testing, rollback sab main? Aur aap?”
Manager: “I will ask ETA every five minutes.”
Junior: “Sir, ek command mein kar denge.”
Senior: “Last time printer bhi cluster join kar gaya tha!”


## Scene 03 — Chintu receives production access (2:00)

**Action:** Read-only request mistakenly becomes cluster administrator.

**Dialogue / beats:**
Junior: “Sir, read-only access chahiye.”
Lead: “Request mein cluster administrator likha hai. Same thing?”
Senior: “Bilkul same nahi hai!”
Manager approves distractedly.
Junior: “Wow, production access!”
Senior: “Sirf status dekhna, kuch delete mat karna.”
Junior: “Itne pods! Electricity kha rahe honge.”
Senior: “Pod aur fan mein difference hota hai, beta.”


## Scene 04 — The Kubernetes disaster (2:00)

**Action:** Chintu deletes application pods; controllers recreate them but readiness fails.

**Dialogue / beats:**
[On-screen simulated terminal, never a real production environment: kubectl delete pods --all -n production]
Junior: “Sir! 35 pods se zero. Cost saving!”
Senior: “TUNE KYA KIYA?!”
Junior: “Housekeeping, sir.”
Manager: “Can we undelete?”
Senior: “Recycle bin nahi hai!”
[Controllers recreate pods; some readiness checks fail; alert storm.]


## Scene 05 — Emergency bridge call (2:00)

**Action:** Thirty-six attendees, mute confusion and embarrassing screen share.

**Dialogue / beats:**
Lead: “Hello, am I audible?”
Manager speaks while muted.
Senior: “PRODUCTION DOWN HAI!”
Manager: “P1 or P2? ETA?”
Senior: “Customer payments fail ho rahe hain!”
Junior shares tabs: undo kubectl delete, resign professionally, Himalaya flights.
Manager: “Why Himalaya?”
Junior: “Disaster recovery location, sir.”


## Scene 06 — The Senior investigates (2:00)

**Action:** Senior traces service and ingress routing, discovers wrong backend.

**Dialogue / beats:**
Senior checks deployments, pods, services, ingress and events.
Senior: “Pods recreate ho rahe hain, traffic wrong backend pe ja raha hai.”
Lead: “Network issue or Kubernetes issue?”
Senior: “Investigate karne do!”
Manager: “Can we assign ownership?”
Senior: “Problem ko chair de dete hain.”
Junior: “Ingress fix karna chahiye?”
Senior: “Pehli baar sahi bola.”
Junior: “YouTube se seekha.”
Senior: “Tareef wapas.”


## Scene 07 — The change approval circus (2:00)

**Action:** Emergency CAB discussion and exaggerated bureaucracy.

**Dialogue / beats:**
Approver: “Business justification?”
Senior: “Customers ko application use karni hai.”
Approver: “Risk if rejected?”
Senior: “Down rahegi.”
Approver: “Risk if approved?”
Senior: “Chal sakti hai.”
Approver: “Let's schedule another meeting.”
Lead: “Ticket create karta hoon.”
Senior: “Retirement application create karta hoon.”


## Scene 08 — The network blame game (2:00)

**Action:** F5, gateway, ingress and service visualized as a packet maze.

**Dialogue / beats:**
Network: “Humari side green hai.”
Security: “Firewall fine.”
Application: “Code fine.”
Manager: “Then whose issue?”
[Everyone points to DevOps.]
Senior: “Sab green hai toh production red kyun?”
Junior: “Red green mila ke yellow kar dein?”
[Packet scooter traverses F5, gateway, ingress, service, wrong backend.]


## Scene 09 — ArgoCD strikes back (2:00)

**Action:** Manual hotfix reverts because Git desired state remains incorrect.

**Dialogue / beats:**
Senior fixes ingress manually under emergency approval. Dashboard green, then red.
Argo Robot: “Out of sync. Restoring desired state.”
Junior: “Robot ne aapka fix undo kar diya!”
Senior: “Git mein purani config hai!”
Lead: “Can we ask ArgoCD to stop?”
Argo Robot: “I am doing exactly what you told me to do.”
[Senior updates Git, validates and syncs.]


## Scene 10 — The Junior unexpected solution (2:00)

**Action:** Chintu identifies wrong readiness path; GitOps fix deployed.

**Dialogue / beats:**
Manager: “Any update?”
Senior: “Same update jo 27 baar diya.”
Junior: “Readiness probe wrong path pe hai. App uses /health/ready, probe uses /ready.”
Senior: “Chintu... tu sahi hai.”
Junior: “Sir repeat please, recording on karoon?”
[Team reviews Git change and deploys.]
Senior: “Good job, beta.”
Junior: “Promotion?”
Senior: “Pehle probation.”


## Scene 11 — Production restored (2:00)

**Action:** Green checks, celebration and manager takes credit.

**Dialogue / beats:**
Lead: “Production stable!”
Manager: “Teamwork makes the dream work.”
Senior: “Aapne kya kiya?”
Manager: “Stakeholder confidence.”
Junior: “Confidence se pods start hote hain?”
Executive: “Who led recovery?”
Manager: “I personally supervised.”
Manager: “Employee of the month goes to... myself!”
[Confetti and deadpan reaction montage.]


## Scene 12 — The Terraform twist (1:00)

**Action:** Chintu reveals disaster recovery destroy plan was applied.

**Dialogue / beats:**
Junior: “Sir, one small doubt. DR environment optimize karna allowed?”
Senior: “Kyun?”
Junior: “Terraform plan: 0 add, 0 change, 47 destroy.”
Senior: “Apply toh nahi kiya?”
Junior: “Pehle kiya tha. Ab pooch raha hoon.”
[Blackout. DEVOPS 2: THE TERRAFORM REVENGE.]


## Scene 13 — Credits and mountain stinger (1:00)

**Action:** Senior receives a new message while resting in Himalayas.

**Dialogue / beats:**
[40 seconds original music, credits and funny outtakes.]
Senior relaxes in Himalayas: “Finally no alerts, no deployments, no Chintu.”
Text from Junior: “Sir, production cluster delete ho gaya toh restore kaise?”
[Senior screams, avalanche. THE END.]
