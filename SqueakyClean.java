class SqueakyClean {
    static String clean(String identifier) {
        
        StringBuilder res = new StringBuilder();
        char[] characters = identifier.toCharArray();

        for (int i = 0; i < characters.length; i++) {
            char current = characters[i];
            String currentString = Character.toString(current);

            if (Character.isSpaceChar(current)) {
                res.append('_');
            }
            else if (Character.isISOControl(current)) {
                res.append("CTRL");
            }
            else if (current == '-' && i < characters.length - 1 && Character.isLetter(characters[i + 1])) {
                res.append(Character.toUpperCase(characters[i + 1]));
                i++;
            }
            else if (currentString.matches("\\p{InGreek}") && Character.isLowerCase(current)) {
                continue;
            }
            else if (!Character.isLetter(current)) {
                continue;
            }
            else {
                res.append(current);
            }
        }

        return res.toString();
    }
}