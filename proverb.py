def proverb(*input_data, qualifier=None):
    rs = ["For ", "want ", "of ", "a ", "the ", "was ", "lost."]
    fs = ["And ", "all ", "for ", "the ", "want ", "of ", "a "]
    result = []

    if not input_data:
        return []

    if len(input_data) == 1:
        # Single input, with or without qualifier
        prefix = f"{qualifier} " if qualifier else ""
        line = "".join(fs) + prefix + input_data[0] + "."
        result.append(line)
    else:
        # Multiple inputs
        for i in range(len(input_data) - 1):
            line = (
                "".join(rs[0:4]) + input_data[i] + " " +
                rs[4] + input_data[i + 1] + " " + rs[5] + rs[6]
            )
            result.append(line)
            
        # Final line, with qualifier if provided
        prefix = f"{qualifier} " if qualifier else ""
        final_line = "".join(fs) + prefix + input_data[0] + "."
        result.append(final_line)

    return result
        
      
    