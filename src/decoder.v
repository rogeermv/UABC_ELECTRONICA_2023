
/*
      -- 1 --
     |       |
     6       2
     |       |
      -- 7 --
     |       |
     5       3
     |       |
      -- 4 --
*/

module seg7 (
    input wire [3:0] counter,
    output reg [6:0] segments
);

    always @(*) begin
        case(counter)
            0: segments = 7'b0111110; //U
            1: segments = 7'b1110111; //A
            2: segments = 7'b1111100; //B
            3: segments = 7'b0111001; //C
            4: segments = 7'b1000000; //-
            5: segments = 7'b1111001; //E
            6: segments = 7'b0111000; //L 
            7: segments = 7'b1111001; //E
            8: segments = 7'b0111001; //C
            9: segments = 7'b0110001; //T
            10: segments = 7'b1010000; //R
            11: segments = 7'b0111111; //O
            12: segments = 7'b1010100; //N
            13: segments = 7'b0110000; //I
            14: segments = 7'b0111001; //C
            15: segments = 7'b1110111; //A
            default:    
                segments = 7'b0000000;
        endcase
    end

endmodule

