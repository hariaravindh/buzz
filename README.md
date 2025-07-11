<section style="text-align:center; padding:60px 20px; background:#1a237e; color:#fff;">
  <h1 style="font-size:2.5em; margin:0; text-align:center;">BUZZ - Bus Booking System</h1>
  <p style="font-style:italic; margin:15px 0 0; text-align:center;">
    Booking a ride should feel as seamless as clicking a snap, right ?
  </p>
</section>

<section style="max-width:800px; margin:40px auto; padding:0 20px;">
  <h2 style="text-align:center;">Story - The Why ? </h2>
  <p>
    During the lockdown years, my school friend Niranjan and I noticed lack of transparency and transaction control in online bus booking,
    alongside clunky CLI flows, data conflicts & glitchy reservations and zero rollback safety.
    As 11th graders with an idealogy for clean code, we built BUZZ, a Python–MySQL app
    ensuring straight forward reservations, transparent transactions and data integrity.
  </p>
</section>

<section style="max-width:800px; margin:40px auto; padding:0 20px;">
  <h2> Core Features & Architecture</h2>
  <ul style="list-style:none; padding:0;">
    <li style="padding:10px; border-left:4px solid #1a237e;">
      <strong>Smart CLI:</strong>
      <code>book</code>, <code>cancel</code>, <code>status</code>, <code>details</code> structured like professional DVCS tools.
    </li>
    <li style="padding:10px; border-left:4px solid #1a237e;">
      <strong>ACID compliant MySQL backend:</strong>
      clean transactions, rollback safety, data integrity.
    </li>
    <li style="padding:10px; border-left:4px solid #1a237e;">
      <strong>Dynamic schema:</strong>
      Auto creates <code>buses</code>, <code>routes</code>, <code>berth</code>, <code>bookings</code>.
    </li>
    <li style="padding:10px; border-left:4px solid #1a237e;">
      <strong>Real time interactions:</strong>
      live seat counts, immediate commit and feedback.
    </li>
    <li style="padding:10px; border-left:4px solid #1a237e;">
      <strong>Modular codebase:</strong>
      separated into <code>core</code>, <code>models</code> for future evolution.
    </li>
    <li style="padding:10px; border-left:4px solid #1a237e;">
      <strong>Quality toolchain:</strong>
      unit tests + formatting + GitHub Actions CI.
    </li>
  </ul>
</section>

<section style="max-width:800px; margin:40px auto; padding:0 20px;">
  <h2> More Features & Innovation</h2>
  <ul>
    <li>Colorized CLI output with ANSI cues for clear success/error states.</li>
    <li>Fuzzy logic help: Auto suggests commands when typoed.</li>
    <li>Idempotent operations via unique trip hashes to avoid duplicate bookings.</li>
    <li>Debug mode to print SQL and transaction logs.</li>
    <li>Future ready: supports extension via web UI.</li>
  </ul>
</section>


