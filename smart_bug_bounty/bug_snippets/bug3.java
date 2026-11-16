public class BankAccountTransfer {

    public static int calculateProjectedBalance(int currentBalance, int monthlyDeposit, int months) {
        if (months < 0) {
            throw new IllegalArgumentException("Months cannot be negative");
        }
        // Bug 1: Integer overflow when monthlyDeposit * months exceeds Integer.MAX_VALUE
        int totalDeposit = monthlyDeposit * months;
        return currentBalance + totalDeposit;
    }

    public static boolean isAccountActive(String status) {
        // Bug 2: Calling .equals() on potentially null parameter throws NullPointerException
        return status.equals("ACTIVE");
    }
}
