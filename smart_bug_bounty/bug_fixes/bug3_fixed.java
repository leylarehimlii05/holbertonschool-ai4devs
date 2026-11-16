public class BankAccountTransfer {

    public static long calculateProjectedBalance(int currentBalance, int monthlyDeposit, int months) {
        if (months < 0) {
            throw new IllegalArgumentException("Months cannot be negative");
        }
        long totalDeposit = (long) monthlyDeposit * months;
        return (long) currentBalance + totalDeposit;
    }

    public static boolean isAccountActive(String status) {
        return "ACTIVE".equals(status);
    }

    public static void main(String[] args) {
        assert calculateProjectedBalance(1000, 500, 6) == 4000L;
        assert calculateProjectedBalance(100, 1_000_000_000, 3) == 3_000_000_100L;
        assert isAccountActive("ACTIVE");
        assert !isAccountActive(null);
        System.out.println("bug3_fixed.java: All 4 test cases passed!");
    }
}
