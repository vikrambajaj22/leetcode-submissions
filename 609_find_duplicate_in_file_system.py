class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_locations = {}

        for path in paths:
            path_split = path.split(' ')
            directory = path_split[0]
            file_list = path_split[1:]

            for item in file_list:
                file_name = item[:item.index('(')]
                file_content = item[item.index('(')+1:-1]

                if file_content not in content_locations:
                    content_locations[file_content] = [directory+'/'+file_name]
                else:
                    content_locations[file_content] += [directory+'/'+file_name]

        return [group for group in list(content_locations.values()) if len(group) > 1]
