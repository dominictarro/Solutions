/// # Challenge 166: SnowballSH and Cute Arrays
/// 
/// * Difficulty: 3/10
/// * Labels: Prefix Sum
/// 
/// SnowballSH loves arrays. He calls an array "cute" if and only if the sum of the elements in
/// the array is equal to the length of the array. For example, the array [0, 2, 1] is cute,
/// because 0 + 2 + 1 is the length of the array. [3, 1] is not cute, because 3 + 1 is not equal
/// to 2.
/// 
/// SnowballSH has a large array. He wants to know how many non-empty subarrays in that array are
/// "cute." Can you help him?
/// 
/// ## Task
/// 
/// You are given a number T and T testcases follow, for each testcase,
/// 
/// * The first line contains an integer N. This is the number of elements in the array.
/// * The next line contains N integers, separated by a single space. Call this array A. Output a single integer, the number of "cute" non-empty subarrays in A.
/// * Formally, output the number of ordered pairs (i, j) where i <= j and A[i] + A[i+1] + ... + A[j] = length(A).
/// 
/// ## Examples
/// 
/// input
/// ```
/// ‌3
/// 3
/// 0 2 1
/// 6
/// 1 0 0 1 3 1
/// 4
/// 1 1 1 1
/// ```
/// 
/// output
/// ```
/// ‌3
/// 7
/// 10
/// ```
/// 
/// https://discord.com/channels/501090983539245061/680851798340272141/1130473724152393809
pub fn algorithm(n: i32, a: Vec<i32>) -> i32 {
    let mut count = 0;
    for i in 0..n {
        let mut sum = 0;
        for j in i..n {
            sum += a[j as usize];
            if sum == j - i + 1 {
                count += 1;
            }
        }
    }
    count
}
