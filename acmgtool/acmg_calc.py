# path_vs = ['pvs1']
# path_strong = ['ps4', 'ps1', 'ps3', 'ps2']
# path_moderate = ['pm1', 'pm2', 'pm3', 'pm4', 'pm5', 'pm6']
# path_support = ['pp1', 'pp1', 'pp3', 'pp4', 'pp5']
#
# benign_support = ['bp1', 'bp4', 'bp7', 'bp3', 'bp2', 'bp6', 'bp5']
# benign_strong = ['bs1', 'bs2', 'bs3', 'bs4']
# benign_standalone = ['ba1']
#
# # path_assign = None
# # path_a_c_m_g = "VUS"
# # likely_path_assign = None
# # likely_path_a_c_m_g = "VUS"
# # ben_assign = None
# # ben_a_c_m_g = "VUS"
# # likely_ben_assign = None
# # likely_ben_a_c_m_g = "VUS"
#
# print("Input codes: ", data)


def printa(*args):
    for arg in args:
        if arg:
            return "".join(arg)


def printacmgcode(codes):
    return list(map(printa, codes))


def main(data, benign_strong_count=0, benign_support_count=0, benign_standalone_count=0, pathvs_count=0,
         pathstrong_count=0, pathmod_count=0, pathsup_count=0):
    path_vs = ['pvs1']
    path_strong = ['ps4', 'ps1', 'ps3', 'ps2']
    path_moderate = ['pm1', 'pm2', 'pm3', 'pm4', 'pm5', 'pm6']
    path_support = ['pp1', 'pp1', 'pp3', 'pp4', 'pp5']

    benign_support = ['bp1', 'bp4', 'bp7', 'bp3', 'bp2', 'bp6', 'bp5']
    benign_strong = ['bs1', 'bs2', 'bs3', 'bs4']
    benign_standalone = ['ba1']
    allpvs, allps, allpm, allpp, allbs, allbss, allba = ([] for i in range(7))
    codes = []

    # path_assign = None
    # path_a_c_m_g = "VUS"
    # likely_path_assign = None
    # likely_path_a_c_m_g = "VUS"
    # ben_assign = None
    # ben_a_c_m_g = "VUS"
    # likely_ben_assign = None
    # likely_ben_a_c_m_g = "VUS"

    # print("Input codes: ", data)

    for code in data:
        if code in path_vs:
            pathvs_count += 1
            allpvs.append(code)
            codes.append(code)

        elif code in path_strong:
            pathstrong_count += 1
            allps.append(code)
            codes.append(code)
        elif code in path_moderate:
            pathmod_count += 1
            allpm.append(code)
            codes.append(code)
        elif code in path_support:
            pathsup_count += 1
            allpp.append(code)
            codes.append(code)
        elif code in benign_strong:
            benign_strong_count += 1
            allbs.append(code)
            codes.append(code)
        elif code in benign_support:
            benign_support_count += 1
            allbss.append(code)
            codes.append(code)
        elif code in benign_standalone:
            benign_standalone_count += 1
            allba.append(code)
            codes.append(code)

                
    pathstatus = checkpathogenic(pathvs_count, pathsup_count, pathmod_count, pathsup_count)
    likelypathstatus = checklikelypathogenic(pathvs_count, pathsup_count, pathmod_count, pathsup_count)
    benignstatus = checkbenign(benign_strong_count, benign_strong_count, benign_standalone_count)
    likelybenignstatus = chekclikelybenign(benign_strong_count, benign_strong_count, benign_standalone_count)

    reason = printacmgcode(codes)

    result = classify(pathstatus, likelypathstatus, benignstatus, likelybenignstatus)

    return [result,reason]



def checkpathogenic(pathvs_count, pathstrong_count, pathmod_count, pathsup_count):
    if (pathvs_count == 1 and
            (pathstrong_count >= 1 or
                     pathmod_count >= 2 or
                 (pathmod_count == 1 and pathsup_count == 1) or
                     pathsup_count >= 2)) or \
            (pathstrong_count >= 2) or (pathstrong_count == 1 and
                                            (pathmod_count >= 3 or
                                                 (pathmod_count == 2 and pathsup_count >= 2) or
                                                 (pathmod_count == 1 and pathsup_count >= 4))):

        return "assigned"
    else:
        return None


def checklikelypathogenic(pathvs_count, pathstrong_count, pathmod_count, pathsup_count):
    if (pathvs_count == 1 and pathmod_count == 1) or \
            (pathstrong_count == 1 and pathmod_count <= 2) or \
            (pathstrong_count == 1 and pathsup_count >= 2) or \
            (pathmod_count >= 3) or \
            (pathmod_count == 2 and pathsup_count >= 2) or \
            (pathmod_count == 1 and pathsup_count >= 4):

        return "assigned"
    else:
        return None


def checkbenign(benign_strong_count, benign_support_count, benign_standalone_count):
    if benign_standalone_count == 1 or benign_strong_count >= 2:

        return "assigned"
    else:
        return None


def chekclikelybenign(benign_strong_count, benign_support_count, benign_standalone_count):
    if (benign_strong_count == 1 and benign_support_count == 1) or benign_support_count >= 2:

        return "assigned"
    else:
        return None


def classify(path, lpath, ben, lben):
    if (path == "assigned" or lpath == "assigned") and \
            (ben == "assigned" or lben == "assigned"):
        return "VUS - conflicting evidences"
    elif path == "assigned":
        return "Pathogenic"
    elif lpath == "assigned":
        return "Likely Pathogenic"
    elif ben == "assigned":
        return "Benign"
    elif lben == "assigned":
        return "Likely Benign"
    else:
        return "Not enough evidence"


if __name__ == '__main__':
    lp = "BP1, BP4, PM3, PP1, PS4".lower().split(", ")
    print(main(lp))
