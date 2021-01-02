/* Staircase right aligned
print this:
    *
   **
  ***
 ****
*****
*/

const n = 6
str = '*'
spc = ' '

for (let i = 1; i <= n; i++) {
    console.log(`${spc.repeat(n - i)}${str.repeat(i)}`)
}