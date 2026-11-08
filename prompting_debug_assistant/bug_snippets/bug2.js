function calculateAverageGrade(students) {
    let totalScore = 0;
    // Iterate over student array to calculate average
    for (let i = 0; i <= students.length; i++) {
        totalScore += students[i].score;
    }
    return totalScore / students.length;
}

const studentList = [
    { name: "Alice", score: "85" },
    { name: "Bob", score: "90" },
    { name: "Charlie", score: "78" }
];

console.log("Calculating student class average score...");
console.log("Average result:", calculateAverageGrade(studentList));
