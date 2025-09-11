# kata: https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
def pick_peaks(arr):
    pos = []
    peaks = []
    n = len(arr)

    i = 1
    while i < n - 1:

        if arr[i] > arr[i - 1]:

            if arr[i] > arr[i + 1]:
                pos.append(i)
                peaks.append(arr[i])
                i += 1

            elif arr[i] == arr[i + 1]:
                plateau_start = i

                while i < n - 1 and arr[i] == arr[i + 1]:
                    i += 1

                if i < n - 1 and arr[i] > arr[i + 1]:
                    pos.append(plateau_start)
                    peaks.append(arr[plateau_start])
        i += 1

    return {"pos": pos, "peaks": peaks}
