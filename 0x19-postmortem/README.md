# Postmortem: Database Service Outage on 2024-08-18


## Issue Summary

- **Duration:** The outage lasted for 3 hours, from 08:15 AM to 11:15 AM UTC on 2024-08-18.
- **Impact:** The primary database service was down, resulting in 100% unavailability of all web applications relying on this database. Users experienced complete service interruption with inability to access any features. Approximately 85% of the total user base was affected.
- **Root Cause:** The root cause was a deadlock in the database cluster caused by a misconfigured failover during a routine maintenance operation.

---

## Timeline

- **08:15 AM UTC:** Monitoring alert triggered, indicating a significant spike in database response times.
- **08:16 AM UTC:** Issue confirmed by an engineer after noticing that the web applications were non-responsive.
- **08:20 AM UTC:** Initial investigation started, focusing on network issues potentially causing slow database communication.
- **08:40 AM UTC:** Misleading debug path taken, investigating possible DDoS attack due to unusual traffic patterns.
- **09:00 AM UTC:** Escalated to the Database Operations Team after ruling out network and DDoS-related causes.
- **09:15 AM UTC:** Discovered that a routine failover did not complete properly, causing a deadlock.
- **10:00 AM UTC:** Database cluster reconfiguration initiated to resolve the deadlock.
- **11:15 AM UTC:** Full service restored after database recovery and verification of all dependent services.

---

## Root Cause and Resolution

- **Root Cause:** The root cause of the outage was a deadlock condition in the database cluster during a scheduled failover. The failover was triggered as part of routine maintenance, but due to a misconfiguration in the failover script, the secondary node did not come online as expected. This caused a cascading effect, where the primary node was overloaded, leading to a deadlock that prevented any read/write operations.
  
- **Resolution:** The issue was resolved by manually reconfiguring the database cluster to break the deadlock. This involved restarting the affected nodes and re-running the failover process with corrected configurations. Once the cluster was stable, extensive testing was conducted to ensure data integrity and full restoration of services.

---

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Review and update failover scripts to prevent similar misconfigurations.
  - Enhance monitoring on database failover processes to detect and alert on incomplete transitions.
  - Conduct a thorough review of the current database cluster configuration for other potential risks.

- **Action Items:**
  - [ ] Patch the failover script to handle edge cases in node transitions.
  - [ ] Implement automated testing of failover procedures during maintenance windows.
  - [ ] Add detailed logging for failover processes to aid in faster diagnosis in future incidents.
  - [ ] Schedule training for the operations team on recent changes to the failover procedure.
  - [ ] Perform a disaster recovery drill to test new configurations under load conditions.
