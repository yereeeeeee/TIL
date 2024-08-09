import java.io.*;
import java.util.*;

class UserSolution {
    static HashMap<Integer, PriorityQueue<Player>> bestMember = new HashMap<>();
    static HashMap<Integer, PriorityQueue<Player>> worstMember = new HashMap<>();
    static int leagueNum;
    void init(int N, int L, int mAbility[]) {
        leagueNum = N/L;
        for (int i = 0; i < leagueNum; i++) {
            bestMember.put(i, new PriorityQueue<>());
            worstMember.put(i, new PriorityQueue<>());
            for (int j = i; j < L+i; j++) {
                bestMember.get(i).offer(new Player(j, mAbility[j]));
                bestMember.get(i).offer(new Player(j, -1 * mAbility[j]));
            }
        }
    }

    int move() {
        int sumId = 0;

        for (int i = 1; i < leagueNum - 1; i++) {
            Player bestPlayer = bestMember.get(i).peek();
            Player worstPlayer_top = worstMember.get(i-1).peek();
            Player worstPlayer = worstMember.get(i).peek();
            Player bestPlayer_bot = bestMember.get(i+1).peek();
        }


        return 0;
    }

    int trade() {
        return 0;
    }

    class Player {
        int id;
        int ability;

        public Player(int id, int ability) {
            this.id = id;
            this.ability = ability;
        }
    }

}