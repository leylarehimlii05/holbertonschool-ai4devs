# User Stories: CarpoolConnect

### User Story 1
As an employee, I want to register and log in using my corporate email or SSO so that I only share rides with verified coworkers.
**Acceptance Criteria**:
- User can authenticate using their company email domain or corporate SSO.
- Unverified external email domains are automatically rejected.
- User profile displays a "Verified Employee" badge upon successful login.
**Priority**: MVP

### User Story 2
As a corporate driver, I want to post my daily commute route and available seats so that coworkers along my route can request a ride.
**Acceptance Criteria**:
- Driver can specify start location, office destination, departure time, and number of available seats (1–4).
- Route is saved and becomes immediately searchable by verified coworkers.
- Driver can edit or cancel a scheduled ride up to 30 minutes before departure.
**Priority**: MVP

### User Story 3
As a corporate passenger, I want to search for drivers heading to my office along my route so that I can find a reliable daily ride.
**Acceptance Criteria**:
- Passenger enters home pickup location, office destination, and desired arrival time.
- System displays matching drivers within a 3 km detour radius and +/- 20 minutes of the target schedule.
- Ride request can be submitted in under 2 minutes.
**Priority**: MVP

### User Story 4
As a corporate driver, I want to review and approve or decline incoming ride requests so that I maintain control over who rides in my vehicle.
**Acceptance Criteria**:
- Driver receives an instant notification when a passenger requests a seat.
- Driver can view the passenger's department, verified badge, and rating before deciding.
- Approving a request automatically decrements the available seat count by one.
**Priority**: MVP

### User Story 5
As a corporate passenger, I want to split fuel and toll costs automatically within the app so that I can pay my fair share without awkward cash exchanges.
**Acceptance Criteria**:
- System calculates a transparent per-passenger cost share based on distance and standard fuel rates.
- Payment is processed automatically upon trip completion via linked payment method or commuter wallet.
- Both driver and passenger receive a digital receipt after the trip.
**Priority**: High

### User Story 6
As a regular commuter, I want to set up recurring weekday ride schedules so that I do not have to re-book my commute every single day.
**Acceptance Criteria**:
- Users can select specific weekdays (e.g., Monday–Friday) for a recurring ride offer or request.
- System automatically generates daily trip instances for the upcoming week.
- Users can skip or modify a single day without canceling the entire recurring schedule.
**Priority**: High

### User Story 7
As a passenger or driver, I want to rate and review my carpool partner after each trip so that community trust and safety standards remain high.
**Acceptance Criteria**:
- Both parties are prompted to leave a 1-to-5-star rating and optional comment after ride completion.
- Average user ratings are visible on profiles during ride matching.
- Users rated below 3.0 stars are flagged for HR/admin review.
**Priority**: High

### User Story 8
As an HR or Sustainability Manager, I want to view a dashboard of total shared rides and CO₂ emissions saved so that I can include accurate metrics in our annual ESG report.
**Acceptance Criteria**:
- Admin dashboard displays total shared trips, total kilometers saved, and estimated CO₂ reduction in kilograms.
- Data can be filtered by date range, department, or office location.
- Metrics can be exported as a CSV or PDF report.
**Priority**: High

### User Story 9
As a passenger, I want to share my live trip status and vehicle details with a trusted contact so that I feel safe during my commute.
**Acceptance Criteria**:
- Passenger can generate a live tracking link showing route progress, driver name, and license plate number.
- Tracking link expires automatically once the trip is marked as completed.
- Feature is accessible directly from the active ride screen in one tap.
**Priority**: Medium

### User Story 10
As a corporate driver, I want to earn company sustainability points for every shared commute so that I can redeem them for reserved parking or workplace perks.
**Acceptance Criteria**:
- Driver earns a fixed number of eco-points per completed carpool trip.
- Points balance is displayed on the user's profile dashboard.
- Accumulated points can be redeemed for company-configured rewards (e.g., priority parking pass, cafeteria vouchers).
**Priority**: Low
