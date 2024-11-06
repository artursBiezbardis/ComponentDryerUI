class FormatStringUtilities:

    @staticmethod
    def break_string_in_lines(string, max_line_length):
        words = string.split()
        formatted_text = ""
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_length:
                current_line += (" " if current_line else "") + word
            else:
                formatted_text += current_line + "\n"
                current_line = word

        if current_line:
            formatted_text += current_line

        return formatted_text
