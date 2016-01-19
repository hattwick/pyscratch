// Test commit for new repo

package main     // Every Go program must start with a package declaration

import "fmt"    // Import additional libraries.  This is the Format package for i/o formatting
//  import "os"
//  import "os/exec"

const pi = 3.14     // Go supports constants that cannot change

func main() {
    var message string
    message = "Test commit for new repo.\n"
    fmt.Print(message)    

// To get help, try "godoc fmt Println"


    fmt.Print("Enter a number you need to double? ")
    var input float64
    fmt.Scanf("%f", &input)
 
    output := input * 2

    fmt.Println(output)
    
    output +=1      // just add one more 

    fmt.Println(output)


// now adding a for loop.  Does everything have to be in function main?

    for i := 5; i <= 10; i++ {
        fmt.Println(i)
        if i% 2 == 0 {
            fmt.Println(i, "even")
        }  else {
            fmt.Println(i, "odd")
        }
    }

// Moving to the switch

    fmt.Print("\n Now enter your direction of travel?\n")
    var compass string
    fmt.Scanln("%c", &compass)
    
    switch compass {
    case "e": fmt.Println("East")
    case "n": fmt.Println("North")
    default: fmt.Println("You are lost")
    }


// Now the array.  Let's build an array to average 5 numbers

    var num [5]float64
        num[0] = 49
        num[1] = 42
        num[2] = 30
        num[3] = 28
        num[4] = 38

    var total float64 = 0
    for i := 0; i <5; i++ {
        total += num[i]
        fmt.Println("running total: ", total)
    }
    fmt.Println(total / 5)


}

// --30--
ubuntu@ip-